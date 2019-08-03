# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: HAI5KOR
Date: 8th May 2019
Description: First Version of Agents
"""

# 1, Create 1 NGO User
# 2. Create 3 Users with devices
# 2.5 Display user profile and wallet    
# 3. Trigger an auction with preferences (NGO User) --> SC
    #3.5 Broadcast to all users
# 4. User bidding at time start (bid amount, duration) [low exact high] (User)
# 5. Wait for period (NGO)
# 6. Close Auction --> (SC)
# 7. Analyze winner bids --> (SC)
# 8. Infrom Users (NGO)
# 9. Wait for TOff + DelT, Trigger Settlement (NGO)
#10. Poll Broadcast/Event (User)
#11. Check to participate in Auction (User)
#12. Bid for Auctions (User)
#13. Intimation of winning (User)
#14. User action during Off Period (User) 
#%% Importing Required Libraries
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import datetime
import sys
from enum import Enum
import random

from NGO import NGOClass
from UserClass import UserClass
#%% Creating common functions and constants

BidDuration = 30 #Time in seconds for which bid is active
SwitchOffDuration = 30 #Time in seconds for which appliances should be off
BidSwitchingDelay = 40 # Time in seconds between Bid end and Switch off 

NumAuctions = 3

def generateRandom(TypeRdm):
    Id = random.randint(1,100000)
    Id = TypeRdm + str(Id).zfill(5)
    return Id

class UserDef(Enum):
    NGO = 0
    User = 1
    
class DeviceDef(Enum):
    Fridge = 0
    HVAC = 1
    
DeviceAddress = ['0x895aE9efB156e388Bd324e466576285906d20827',
                 '0x9aeC04AEa530111F337f3D121488f22383098627',
                 '0x263a5223a294C64b5E48Cab164e95131938C87ea',
                 '0x628B31Bc31d04f425fb93209AFA332e893735184',
                 '0x0b5f0D1a4CD335cBDE8A0a6A2A99a9D20518aF81',
                 '0x19D0e3a5b42032217649D73ab4398d9892d6BB10',
                 '0x40C9976E63A0D43a67095222171b40E4D5AC8CBC',
                 '0x64009E29507c27133Efb995BE1a3993b5548b175',
                 '0x8aB8151D7Fd54d0567AD5bE17cc4173da43E9F30',
                 '0x585d47A02047ED10FeC50b5F6001de02Ad06d377']
#%%
# Create 1 NGO User
# TO-DO: Create random numbers for user_id, device_id --> Done

UserId = generateRandom("USR")
DevId = generateRandom("DEV")

NGO_Object = NGOClass(user_id = UserId,
                           address = DeviceAddress[0],
                           user_type = UserDef.NGO.value,
                           device_id = DevId,
                           device_type = DeviceDef.Fridge.value,
                           Total_Incentive = 100,
                           WHGoal = 1000) #Created User object


NGO_Object.generateNGO()
      
#%% 2. Create n Users with devices
# TO-DO: Create random numbers for user_id, device_id --> Done

maxUsers = 9 #address exists for 10 users with NGO being the first user
Device_Type_List = [DeviceDef.Fridge.value, #User1
                    DeviceDef.HVAC.value, #User2
                    DeviceDef.HVAC.value, #User3
                    DeviceDef.Fridge.value, #User4
                    DeviceDef.HVAC.value, #User5
                    DeviceDef.HVAC.value, #User6
                    DeviceDef.Fridge.value, #User7
                    DeviceDef.HVAC.value, #User8
                    DeviceDef.HVAC.value] #User9

DeviceRated_Wattage = [200, #User1
                  200, #User2
                  200, #User3
                  200, #User4
                  200, #User5
                  200, #User6
                  200, #User7
                  200, #User8
                  200] #User9

User_Incentive_List = [10, #User1
                  50, #User2
                  150, #User3
                  50, #User4
                  100, #User5
                  100, #User6
                  100, #User7
                  100, #User8
                  100] #User9

User_OffDuration_List = [10, #User1
                  10, #User2
                  10, #User3
                  10, #User4
                  10, #User5
                  10, #User6
                  10, #User7
                  10, #User8
                  10] #User9

Full_User_List = []
for i in range(maxUsers): #replace with maxUsers to run auction with all users 
    UserId = generateRandom("USR")
    DevId = generateRandom("DEV")

    User_Obj = UserClass(user_id = UserId,
                           address = DeviceAddress[i+1], #first index belongs to NGO
                           user_type = UserDef.User.value,
                           device_id = DevId,
                           device_type = Device_Type_List[i],
                           BidWin = False,
                           Watt = DeviceRated_Wattage[i],
                           Incentive = User_Incentive_List[i],
                           UserOffDuration = User_OffDuration_List[i])
    
    User_Obj.generateUser()
    Full_User_List.append(User_Obj)
# ----------------------------------------------------------------------------
'''
UserId = generateRandom("USR")
DevId = generateRandom("DEV")

User2_Obj = UserClass(user_id = UserId,
                           address = DeviceAddress[2],
                           user_type = UserDef.User.value,
                           device_id = DevId,
                           device_type = DeviceDef.HVAC.value,
                           BidWin = False,
                           Watt = 200,
                           Incentive = 50,
                           UserOffDuration = 10)

# ----------------------------------------------------------------------------

UserId = generateRandom("USR")
DevId = generateRandom("DEV")

User3_Obj = UserClass(user_id = UserId,
                           address = DeviceAddress[3],
                           user_type = UserDef.User.value,
                           device_id = DevId,
                           device_type = DeviceDef.HVAC.value,
                           wallet_balance = 100,
                           BidWin = False,
                           Watt = 200,
                           Incentive = 150,
                           UserOffDuration = 10)

'''
# ----------------------------------------------------------------------------    
# 2.5 Display user profile and wallet
#TO-DO: Wallet information to be added --> Done
# Register Users to NGO
'''
print("User1:")
User_List[0].getDetails()

print("User2:")
User_List[1].getDetails()

print("User3:")
User_List[3].getDetails()
'''

#%% 3. Trigger an auction with preferences (NGO User) --> SC
# create an instance of the API class

# TO-DO: Create random numbers for auction_id --> Done

#TO-DO: to be included from NGO preferences

'''
NGO_Object.AddUserList(User1_Obj)
NGO_Object.AddUserList(User2_Obj)
NGO_Object.AddUserList(User3_Obj)
'''

for AucIdx in range(NumAuctions):
    User_List = []
    NoOfUsers = random.randint(2,9)
    SelectedIndex = random.sample(range(0,9),NoOfUsers)
    SelectedIndex.sort()
    
    for UserSelIdx in SelectedIndex:
        User_List.append(Full_User_List[UserSelIdx])
    
    for i in range(len(User_List)):
        print("User ",i+1)
        User_List[i].getDetails()
        NGO_Object.AddUserList(User_List[i])
    
    print("Starting New Auction!")
    AucId = generateRandom("AUC")
    
    bid_start = int(time.time())
    bid_end = bid_start + BidDuration #Bid ends in 1 minute
    off_start = bid_end + BidSwitchingDelay #Off Period starts 6 seconds after bidding ends
    off_end =  off_start + SwitchOffDuration #Off Period ends 18 seconds after start
    
    NGO_Object.TriggerAuction(AucId,bid_start,bid_end,off_start,off_end)
    #%% 3.5 Broadcast to all users
    # TO-DO try pubsub mechanism
    time.sleep(1) #Time to broadcast Auction start to all users
    print("Bidding under Process ...")
    #%% 4. User bidding at time start (bid amount, duration) [low exact high] (User)
    # User 1 Bidding: Low Bid
    
    # TO-DO: Create random numbers for bid_id --> Done
    
    # create an instance of the API class
    '''
    BidId = generateRandom("BID")
    
    User1_Obj.generateBid(bid_id = BidId,auction_id = AucId, offstart=off_start,offend = off_end)
    # ----------------------------------------------------------------------------
    # User 2 Bidding: Medium Bid
    
    # create an instance of the API class
    BidId = generateRandom("BID")    
        
    User2_Obj.generateBid(bid_id = BidId,auction_id = AucId, offstart=off_start,offend = off_end)
        
    # ----------------------------------------------------------------------------
    # User 3 Bidding: High Bid
    
    # create an instance of the API class
    BidId = generateRandom("BID")
    
    User3_Obj.generateBid(bid_id = BidId,auction_id = AucId, offstart=off_start,offend = off_end)
    '''
    
    for i in range(len(User_List)):
        BidId1 = generateRandom("BID")
        User_List[i].generateBid(bid_id1 = BidId1,auction_id = AucId, offstart=off_start,offend = off_end)
    #%% Wait for period (NGO)
    print("Waiting for Bid Period to End")
    BidInProgress = True
    progress = 0
    
    #TimeInterval = int((bid_end - currentTime)/10)
    
    #TO-DO: Incorporate a wait bar
    # Capturing Data before bidding ends
    
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
    #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    #%%-------------------------------------------------------------------------
        
    while BidInProgress:
        
        currentTime = int(time.time())
        if currentTime < bid_end:
    #        progress = int(bid_end - currentTime)
    #        if progress%10 == 0:
    #            sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    #            sys.stdout.flush()
            print("Bid ends in: {} seconds".format(int(bid_end - currentTime)))
            time.sleep(10)
        else:
            BidInProgress = False
    
    
    # Capturing Data after bidding ends
    
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
    #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    #%%-------------------------------------------------------------------------
    
    
    print("Bidding Process ended!")
    time.sleep(2)
    #%% 6. Close Auction --> (SC)
    
    #TO-DO: Implement calling action to close auction
    
    NGO_Object.CloseAuction(AucId)
    print("Smart Contract Intimated for closing the auction")
    
    #%% 7. Analyze winner bids --> (SC)
    #%% 8. Infrom Users (NGO)
    
    ListOfWiners = NGO_Object.getWinnerList(AucId)
    
    print("List of Winners: ")
    for i in ListOfWiners:
        print(i.user_id)
    
    #%% 9. Wait for TOff + DelT
    OffPeridStart = True
    while OffPeridStart:
        currentTime = int(time.time())
        if currentTime < off_start:
    #        progress = int(bid_end - currentTime)
    #        if progress%10 == 0:
    #            sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    #            sys.stdout.flush()
            print("Off Perid starts in: {} seconds".format(int(off_start - currentTime)))
            time.sleep(20)
        else:
            OffPeridStart = False
            
    print("\n Off Period Starts!")
    
    User_List[0].Watt = 0
    User_List[1].Watt = 0
    OffPeridEnd = True
    Flag = True
    #TO-DO: inform the devices to switch off
    #TO-DO: inform the smart contract of the watt consumption of the devices
    while OffPeridEnd:
    
    
        currentTime = int(time.time())
        if currentTime < off_end:
    #        progress = int(bid_end - currentTime)
    #        if progress%10 == 0:
    #            sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    #            sys.stdout.flush()
            print("Off Period ends in: {} seconds".format(int(off_end - currentTime)))
            for i in range(len(User_List)):
                UsgId = generateRandom("USG")
                # Get the device usage and pass to SC: Device are on State
                #%% Replace with actual Data --------------------------------------------
                User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
                if User_List[i].BidWin:
                    print("User {} Consumption {} W".format(User_List[i].user_id,User_List[i].Watt))
                #%%-------------------------------------------------------------------------
            
            time.sleep(20)
        else:
            OffPeridEnd = False
    
    #%% ----------------------------------------------------------------------
    User_List[0].Watt = 100
    User_List[1].Watt = 100
    #%% -----------------------------------------------------------------------
    #Closing the auction
    NGO_Object.CloseAuctionPledge(AucId)
    
    print("Smart Contract Intimated for closing the auction")
    
    # Logging data after auction
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
    #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    #%%-------------------------------------------------------------------------
    
    #TO-DO display the total amount of energy saved
    print("\n Off Period Ends! Thank you for saving Energy!") 
    time.sleep(1)       
    #%% 10. Settlement
    #TO-DO: Inform SC of end of OffPeriod and trigger settlement in SC
    print("\nSettlement Details!")
    api_instance = swagger_client.UserApi()
    user_id = NGO_Object.address # str |  (optional)
    
    try:
        api_response1 = api_instance.get_users(user_id=user_id)
        #pprint(api_response1)
    except ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
        
    WalletBalanceList = api_response1[0].wallet_balance
    
    print("NGO Id: {}, Wallet: {}".format(NGO_Object.user_id,WalletBalanceList)) 
    
    for UserIdx in User_List:
        user_id = UserIdx.address # str |  (optional)
    
        try:
            api_response1 = api_instance.get_users(user_id=user_id)
            #pprint(api_response1)
        except ApiException as e:
            print("Exception when calling UserApi->get_users: %s\n" % e)
        
        WalletBalanceList = api_response1[0].wallet_balance
    
        print("USR Id: {}, Wallet: {}".format(UserIdx.user_id,WalletBalanceList)) 
        
#%%
print("\nSettlement Details!")
api_instance = swagger_client.UserApi()
user_id = NGO_Object.address # str |  (optional)
    
try:
    api_response1 = api_instance.get_users(user_id=user_id)
    #pprint(api_response1)
except ApiException as e:
    print("Exception when calling UserApi->get_users: %s\n" % e)
    
WalletBalanceList = api_response1[0].wallet_balance
    
print("NGO Id: {}, Wallet: {}".format(NGO_Object.user_id,WalletBalanceList)) 
    
for UserIdx in Full_User_List:
    user_id = UserIdx.address # str |  (optional)
    
    try:
        api_response1 = api_instance.get_users(user_id=user_id)
            #pprint(api_response1)
    except ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
    
    try:
        WalletBalanceList = api_response1[0].wallet_balance
    
        print("USR Id: {}, Wallet: {}".format(UserIdx.user_id,WalletBalanceList))
    except:
        print("")