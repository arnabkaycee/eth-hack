#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:20:55 2019

@author: himajit
"""

"""
Created on Thu May  9 15:38:55 2019
NGO Class Description
@author: HAI5KOR
"""
import swagger_client
from swagger_client.rest import ApiException
import subprocess

class UserClass:
       
    def __init__(self, user_id = None,
                           address = None,
                           user_type = None,
                           device_id = None,
                           device_type = None,
                           wallet_balance = 0,
                           Incentive = 100,
                           Watt = 200,
                           RatedWatt = 200,
                           BidWin = False,
                           UserOffDuration = 10): #Time for which User1 would switch off his device
        self.user_id = user_id
        self.address = address
        self.user_type = user_type
        self.device_id = device_id
        self.device_type = device_type
        self.wallet_balance = wallet_balance
        self.Incentive = Incentive
        self.Watt = Watt
        self.RatedWatt = RatedWatt
        self.BidWin = BidWin
        self.PledgeWin = False
        self.UserOffDuration = 10
        self.UserBidId = ""
        self.DataTime = []
        self.DataWatt = []
        self.DataAuction = []
        
    def generateUser(self):
        api_instance = swagger_client.UserApi()
        User_Object = swagger_client.User(user_id = self.user_id,
                           address = self.address,
                           user_type = self.user_type,
                           device_id = self.device_id,
                           device_type = self.device_type,
                           wallet_balance = self.wallet_balance) #Created User object
        
        try:
            api_instance.create_user(User_Object)
        except ApiException as e:
            #print("Exception when calling UserApi->create_user: \n") 
            print("Exception when calling UserApi->create_user: %s\n" % e)
        except:
            print("Error1")
    
    def generateBid(self,bid_id1, auction_id, offstart, offend):
       api_instance = swagger_client.AuctionApi()
       
       if offstart + self.UserOffDuration < offend:
           offend = offstart + self.UserOffDuration
           
       User_Bid = swagger_client.Bid(bid_id=bid_id1, 
                          auction_id=auction_id, 
                          user_id=self.address, 
                          bid_amount=self.Incentive, 
                          watt_saving=self.Watt,  
                          off_start_timestamp=offstart, 
                          off_end_timestamp=offend) # Bid  
       #TO-DO: 1. incorporate logic for choosing incentives by individual users (Static or Dynamic)
       #2. Incorporate logic for choosing duration (Static or Dynamic)
       #print("User {} Bidding".format(self.user_id))
       try:
           # Create bid for auction
           api_instance.create_bid(User_Bid)
           self.UserBidId = bid_id1
       except ApiException as e:
           print("Exception when calling AuctionBidApi->post_bid: %s\n" % e)
       except:
           print("Error 6")                   
    
    def UpdateDataAuction(self,offstart,offend):
        if offstart + self.UserOffDuration > offend:
           Duration = offend - offstart
        else:
           Duration = self.UserOffDuration
    
        self.DataAuction.append([offstart,offend,Duration,self.BidWin,self.PledgeWin,self.Incentive,self.Watt])
        
    def logUsageData(self,Watt,UsgId,Flag):
        api_instance = swagger_client.DeviceApi()
        
        if Flag:
            a = str(subprocess.check_output(['bash', 'getPower.sh']))
            FirstIndex = a.find('powerConsumption')
            b = a[FirstIndex:]
            
            if b.find(',') > b.find('}'):
                ThirdIndex = b.find('}')
            else:
                ThirdIndex = b.find(',')


            SecondIndex = b.find(':')
            
            WattValue_Power = float(b[SecondIndex+1:ThirdIndex])
            WattValue_Power = int(WattValue_Power*40)
            #print(WattValue_Power)
        
            usageobj = swagger_client.Body(watt=WattValue_Power,
                               usage_id = UsgId,
                               user_id = self.address) # Body |
        else:
            usageobj = swagger_client.Body(watt=Watt,
                               usage_id = UsgId,
                               user_id = self.address) # Body |

        try:
            # logUsageStats
            api_instance.log_usage_stats(usageobj)
        except ApiException as e:
            print("Exception when logging data: %s\n" % e)
        except:
            print("Error in logging data to SC") 
            
    def getUsageData(self):
        # create an instance of the API class
        api_instance = swagger_client.DeviceApi()
        device_id = self.device_id

        api_response = []
        try:
            api_response = api_instance.get_device_usage(device_id=device_id)
            
        except ApiException as e:
            print("Exception when calling DeviceApi->get_device_usage: %s\n" % e)
        except:
            print("Error getting logged data")
        return api_response
    
    def showWalletBalance(self):
        api_instance = swagger_client.UserApi()
        user_id = self.address # str |  (optional)
    
        try:
            api_response1 = api_instance.get_users(user_id=user_id)
            #pprint(api_response1)
        except ApiException as e:
            print("Exception when calling UserApi->get_users: %s\n" % e)
        
        WalletBalanceList = api_response1[0].wallet_balance
        self.wallet_balance = WalletBalanceList
        #print("USR Id: {}, Wallet: {}".format(self.user_id,WalletBalanceList)) 
        
    def getDetails(self):
        print("\nUser ID: ",self.user_id)
        #print("Address: ",self.address)
        print("User Type: ",self.user_type)
        print("Device ID: ",self.device_id)
        print("Device Type: ",self.device_type)
        #print("Wallet Balance: ",self.wallet_balance)
        print("User Incentive: ",self.Incentive)
        print("Device power: ",self.Watt)
        
    def UpdateDataTime(self,DataTime1):
        self.DataTime.append(DataTime1)
        
    def UpdateDataWatt(self,DataWatt1):
        self.DataWatt.append(DataWatt1)

        
    # Getters and Setters
    def user_id(self):
        return self.user_id
    
    def user_id(self,userid):
        self.user_id = userid
        
    def address(self):
        return self.address
    
    def address(self,address1):
        self.address = address1
        
    def user_type(self):
        return self.user_type
    
    def user_type(self,user_type1):
        self.user_type = user_type1
        
    def device_id(self):
        return self.device_id
    
    def device_id(self,device_id1):
        self.device_id = device_id1
        
    def device_type(self):
        return self.device_type
    
    def device_type(self,device_type1):
        self.device_type = device_type1
        
    def wallet_balance(self):
        return self.wallet_balance
    
    def wallet_balance(self,wallet_balance1):
        self.wallet_balance = wallet_balance1
        
    def Incentive(self):
        return self.Incentive
    
    def Incentive(self,Incentive1):
        self.Incentive = Incentive1
        
    def Watt(self):
        return self.Watt
    
    def Watt(self,Watt1):
        self.Watt = Watt1
    
     
    def BidWin(self):
        return self.BidWin
    
    def BidWin(self,BidWin1):
        self.BidWin = BidWin1
    
    def UserOffDuration(self):
        return self.UserOffDuration
    
    def UserBidId(self):
        return self.UserBidId
    
    def PledgeWin(self):
        return self.PledgeWin
    
    def PledgeWin(self,PledgeWin1):
        self.PledgeWin = PledgeWin1
        
    def DataTime(self):
        return self.DataTime
    
    def DataTime(self,DataTime1):
        self.DataTime = DataTime1
        
    def DataWatt(self):
        return self.DataWatt
    
    def DataWatt(self,DataWatt1):
        self.DataWatt = DataWatt1
        
    def DataAuction(self):
        return self.DataAuction
    
    def DataAuction(self,DataAuction1):
        self.DataAuction = DataAuction1
        
    def RatedWatt(self):
        return self.RatedWatt