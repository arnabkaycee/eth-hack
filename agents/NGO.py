# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:38:55 2019
NGO Class Description
@author: HAI5KOR
"""
import swagger_client
from swagger_client.rest import ApiException

class NGOClass:
       
    def __init__(self, user_id = None,
                           address = None,
                           user_type = None,
                           device_id = None,
                           device_type = None,
                           wallet_balance = 1000,
                           Total_Incentive = 100,
                           WHGoal = 1000):
        self.user_id = user_id
        self.address = address
        self.user_type = user_type
        self.device_id = device_id
        self.device_type = device_type
        self.wallet_balance = wallet_balance
        self.Total_Incentive = Total_Incentive
        self.WHGoal = WHGoal
        self.AuctionCreationObj = None
        self.NGOUser_List = []
        self.AuctionIncentive = []
        self.AuctionWattSec = []
        self.AuctionWatt = []
        
    def generateNGO(self):
        api_instance = swagger_client.UserApi()
        NGO_Object = swagger_client.User(user_id = self.user_id,
                           address = self.address,
                           user_type = self.user_type,
                           device_id = self.device_id,
                           device_type = self.device_type,
                           wallet_balance = self.wallet_balance) #Created User object
        
        try:
            api_instance.create_user(NGO_Object)
        except ApiException as e:
            print("Exception when calling UserApi->create_user: \n") 
            #print("Exception when calling UserApi->create_user: %s\n" % e)
        except:
            print("Error1")
    
    def getDetails(self):
        print("User ID: ",self.user_id)
        print("Address: ",self.address)
        print("User Type: ",self.user_type)
        print("Device ID: ",self.device_id)
        print("Device Type: ",self.device_type)
        print("Wallet Balance: ",self.wallet_balance)
        print("Total Incentive per Auction: ",self.Total_Incentive)
        print("Energy Goal: ",self.WHGoal)
    
    def AddUserList(self,User_Obj):
        self.NGOUser_List.append(User_Obj)
        
    def ClearUserList(self):
        self.NGOUser_List = None
        
    def RemoveUserList(self,index):
        self.NGOUser_List.pop(index)
        
    def CloseAuction(self,AucId):
        api_instance = swagger_client.AuctionApi()
        CloseAuction = swagger_client.Auction(auction_id = AucId) # Auction  

        try:
            api_instance.close_auction(CloseAuction)
        except ApiException as e:
            print("Exception when calling AuctionApi->close_auction: %s\n" % e)
        except:
            print("Error closing auction")
    
    def CloseAuctionPledge(self,AucId):
        api_instance = swagger_client.AuctionApi()
        CloseAuction = swagger_client.Auction(auction_id = AucId) # Auction  

        try:
            api_instance.close_auction_pledge(CloseAuction)
        except ApiException as e:
            print("Exception when calling AuctionApi->close_auction: %s\n" % e)
        except:
            print("Error closing auction pledge")
        
    def getWinnerList(self,AucId):
        api_instance = swagger_client.AuctionApi()
        api_response = []
        # Output type is list of bids
        try:
            api_response = api_instance.get_winning_bids(auction_id=AucId)
            #pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuctionApi->get_winning_bids: %s\n" % e)
        except:
            print("Error in reading Winning Bids")

        strBidIDs = [api_response[x].bid_id for x in range(len(api_response))]
        
        ListOfWiners = []
        for strBids in strBidIDs:
            for usr_list in self.NGOUser_List:
                BidObj = usr_list.UserBidId
                if BidObj == strBids:
                    ListOfWiners.append(usr_list)
                    usr_list.BidWin = True
                    break
        return ListOfWiners
 
    def calculateKPI(self,user_upd_list):
        print("")
        
        
    def TriggerAuction(self,AucId,bid_start,bid_end,off_start,off_end):
        
        UserList_Address = [self.NGOUser_List[x].address for x in range(len(self.NGOUser_List))]
        #print(UserList_Address)
        api_instance = swagger_client.AuctionApi()
        AuctionCreation = swagger_client.Auction(auction_id=AucId, 
                                         users=UserList_Address, 
                                         total_incentive=self.Total_Incentive, 
                                         watt_hour_goal_saving=self.WHGoal, 
                                         bid_start_timestamp=bid_start, 
                                         bid_end_timestamp=bid_end, 
                                         off_start_timestamp=off_start, 
                                         off_end_timestamp=off_end) 
        
        #print("Creating Auction")
        try:
            # Create auction
            api_instance.create_auction(AuctionCreation)
            #print("Auction created with ID: {}".format(AuctionCreation.auction_id))
            self.AuctionCreationObj = AuctionCreation
        except ApiException as e:
            print("Exception when calling AuctionApi->create_auction: %s\n" % e)
        except:
            print("Error5")

    # Getters and Setters
    def user_id(self):
        return self.user_id
    
    def user_id(self,userid):
        self.user_id = userid
        
    def address(self):
        return self.address
    
    def address(self,address):
        self.address = address
        
    def user_type(self):
        return self.user_type
    
    def user_type(self,user_type):
        self.user_type = user_type
        
    def device_id(self):
        return self.device_id
    
    def device_id(self,device_id):
        self.device_id = device_id
        
    def device_type(self):
        return self.device_type
    
    def device_type(self,device_type):
        self.device_type = device_type
        
    def wallet_balance(self):
        return self.wallet_balance
    
    def wallet_balance(self,wallet_balance):
        self.wallet_balance = wallet_balance
        
    def Total_Incentive(self):
        return self.Total_Incentive
    
    def Total_Incentive(self,Total_Incentive):
        self.Total_Incentive = Total_Incentive
        
    def WHGoal(self):
        return self.WHGoal
    
    def WHGoal(self,WHGoal):
        self.WHGoal = WHGoal
        
    def NGOUser_List(self):
        return self.NGOUser_List
    
    def getAuctionCreationObj(self):
        return self.AuctionCreationObj
    
    def AuctionIncentive(self,AuctionIncentive):
        self.AuctionIncentive = AuctionIncentive
        
    def AuctionWattSec(self,AuctionWattSec):
        self.AuctionWattSec = AuctionWattSec
        
    def AuctionWatt(self,AuctionWatt):
        self.AuctionWatt = AuctionWatt