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
import shutil
import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go

from NGO import NGOClass
from UserClass import UserClass
#%% Creating common functions and constants

TerminalSize = shutil.get_terminal_size((80, 20)) #get terminal size to center strings. Used only when running from terminal in Linux

TerminalSize = TerminalSize[0]
DisplayStartString = "="*(TerminalSize)
print(DisplayStartString.center(TerminalSize," "))
print("Welcome to SHAKTI!".center(TerminalSize," "))
print(DisplayStartString.center(TerminalSize," "))

BidDuration = 30 #Time in seconds for which bid is active
SwitchOffDuration = 30 #Time in seconds for which appliances should be off
BidSwitchingDelay = 40 # Time in seconds between Bid end and Switch off 

NumAuctions = 1
UserDisplayWidth = int((TerminalSize - 15)/5)

def getstrtime(timeobj):
    strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeobj))
    return strtime

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

UserId = generateRandom("NGO")
DevId = generateRandom("DEV")

NGO_Object = NGOClass(user_id = UserId,
                           address = DeviceAddress[0],
                           user_type = UserDef.NGO.value,
                           device_id = DevId,
                           device_type = DeviceDef.Fridge.value,
                           Total_Incentive = 200,
                           WHGoal = 50000) #Created User object


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

DeviceRated_Wattage = [100, #User1
                  200, #User2
                  200, #User3
                  100, #User4
                  200, #User5
                  200, #User6
                  100, #User7
                  200, #User8
                  200] #User9

User_Incentive_List = [10, #User1
                  50, #User2
                  150, #User3
                  50, #User4
                  100, #User5
                  20, #User6
                  50, #User7
                  200, #User8
                  100] #User9

User_OffDuration_List = [20, #User1
                  10, #User2
                  10, #User3
                  50, #User4
                  20, #User5
                  10, #User6
                  30, #User7
                  20, #User8
                  40] #User9

print('\n')

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
                           RatedWatt = DeviceRated_Wattage[i],
                           Incentive = User_Incentive_List[i],
                           UserOffDuration = User_OffDuration_List[i])
    
    User_Obj.generateUser()
    Full_User_List.append(User_Obj)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------    
# 2.5 Display user profile and wallet
#TO-DO: Wallet information to be added --> Done
# Register Users to NGO


#%% 3. Trigger an auction with preferences (NGO User) --> SC
# create an instance of the API class

# TO-DO: Create random numbers for auction_id --> Done

#TO-DO: to be included from NGO preferences

NoOfUsers_List = [[0,1,2],
                  [0,1,2,3],
                  [0,1,2,3,4],
                  [0,1,2,3,4,5],
                  [0,1,2,3,4,5,6],
                  [0,1,2,3,4,5,6,7],
                  [0,1,2,3,4,5,6,7,8]]

for AucIdx in range(NumAuctions):
    User_List = []
#    NoOfUsers = random.randint(2,9)
#    SelectedIndex = random.sample(range(0,9),NoOfUsers)
#    SelectedIndex.sort()
    if AucIdx > len(NoOfUsers_List)-1:
        SelectedIndex = NoOfUsers_List[-1]
    else:
        SelectedIndex = NoOfUsers_List[AucIdx]
    
    for UserSelIdx in SelectedIndex:
        User_List.append(Full_User_List[UserSelIdx])
    
    print("\n\n")
    print("USER REGISTRATION".center(TerminalSize,"-"))

    UserTitleString = " "*10 + "|  USER ID".ljust(UserDisplayWidth) + "|  DEVICE ID".ljust(UserDisplayWidth) + "|  DEVICE TYPE".ljust(UserDisplayWidth)  + "|  DEVICE WATTAGE (W)".ljust(UserDisplayWidth) + "|  INCENTIVE (TOKEN)".ljust(UserDisplayWidth)    
    print(UserTitleString)
    UserTitleString = " "*10 + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)  + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)    
    print(UserTitleString)
    
    
    for i in range(len(User_List)):
        #print("User ",i+1)
        #User_List[i].getDetails()
        UserDisplayString = str("USER" + str(i)).ljust(10) +\
        str("|  " + User_List[i].user_id).ljust(UserDisplayWidth) + \
        str("|  " + User_List[i].device_id).ljust(UserDisplayWidth) + \
        str("|  " + DeviceDef(User_List[i].device_type).name).ljust(UserDisplayWidth) + \
        str("|  " + str(User_List[i].Watt)).ljust(UserDisplayWidth) + \
        str("|  " + str(User_List[i].Incentive)).ljust(UserDisplayWidth) 
        print(UserDisplayString)
        print(UserTitleString)
        NGO_Object.AddUserList(User_List[i])
    
    print("\n")
    # Get Previous Balance
    PrevBal = []
    for UserIdx in User_List:
        PrevBal.append(UserIdx.wallet_balance)
    
    # Starting new auction
    print("\n")
    print("AUCTION CREATE".center(TerminalSize,"-"))
    
    AucTitleString = "AUC ID".ljust(10) + "|  BID START TIME".ljust(UserDisplayWidth) + "|  BID STOP TIME".ljust(UserDisplayWidth) + "|  PLEDGE START TIME".ljust(UserDisplayWidth)  + "|  PLEDGE STOP TIME".ljust(UserDisplayWidth) + "|  REWARDS".ljust(UserDisplayWidth)    
    print(AucTitleString)
    
    AucId = generateRandom("AUC")
    
    bid_start = int(time.time())
    bid_end = bid_start + BidDuration #Bid ends in 1 minute
    off_start = bid_end + BidSwitchingDelay #Off Period starts 6 seconds after bidding ends
    off_end =  off_start + SwitchOffDuration #Off Period ends 18 seconds after start
    
    NGO_Object.TriggerAuction(AucId,bid_start,bid_end,off_start,off_end)
    
    AuctionDisplayString = str(AucId).ljust(10) +\
    str("|  " + getstrtime(bid_start)).ljust(UserDisplayWidth) + \
    str("|  " + getstrtime(bid_end)).ljust(UserDisplayWidth) + \
    str("|  " + getstrtime(off_start)).ljust(UserDisplayWidth)  + \
    str("|  " + getstrtime(off_end)).ljust(UserDisplayWidth) + \
    str("|  " + str(NGO_Object.Total_Incentive)).ljust(UserDisplayWidth)    
    print(AuctionDisplayString)
    #%% 3.5 Broadcast to all users
    # TO-DO try pubsub mechanism
    time.sleep(1) #Time to broadcast Auction start to all users
    
    print("\n")
    print("START OF AUCTION".center(TerminalSize,"-"))    

    #%% 4. User bidding at time start (bid amount, duration) [low exact high] (User)
    # User 1 Bidding: Low Bid
    
    # TO-DO: Create random numbers for bid_id --> Done
    
    # create an instance of the API class
    print("\n\n")
    print("BIDDING IN PROGRESS".center(TerminalSize,"-"))
    
    BidTitleString = " "*10 + "|  BID ID".ljust(UserDisplayWidth) + "|  WATTAGE (W)".ljust(UserDisplayWidth) + "|  PLEDGE START TIME".ljust(UserDisplayWidth)  + "|  PLEDGE DURATION (S)".ljust(UserDisplayWidth) + "|  INCENTIVE ASKED (TOKEN)".ljust(UserDisplayWidth)    
    print(BidTitleString)
    BidTitleString = " "*10 + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)  + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)    
    print(BidTitleString)
        
    for i in range(len(User_List)):
        BidId1 = generateRandom("BID")
        User_List[i].generateBid(bid_id1 = BidId1,auction_id = AucId, offstart=off_start,offend = off_end)
        
        BidDisplayString = str("USER" + str(i)).ljust(10) +\
        str("|  " + BidId1).ljust(UserDisplayWidth) + \
        str("|  " + str(User_List[i].Watt)).ljust(UserDisplayWidth) + \
        str("|  " + getstrtime(off_start)).ljust(UserDisplayWidth) + \
        str("|  " + str(User_List[i].UserOffDuration)).ljust(UserDisplayWidth) + \
        str("|  " + str(User_List[i].Incentive)).ljust(UserDisplayWidth) 
        
        print(BidDisplayString)
        print(BidTitleString)
    #%% Wait for period (NGO)
    #print("Waiting for Bid Period to End")
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
    print("\n") 
    
    while BidInProgress:
        
        currentTime = int(time.time())
        if currentTime < bid_end:

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
    print("\n")
    print("END OF BIDDING".center(TerminalSize,"-"))
    time.sleep(1)
    #%% 6. Close Auction --> (SC)
    
    #TO-DO: Implement calling action to close auction
    
    NGO_Object.CloseAuction(AucId)
    
#    print("\n")
#    print("SMART CONTRACT INFORMED FOR CLOSING AUCTION".center(TerminalSize,"-"))
    
    #%% 7. Analyze winner bids --> (SC)
    #%% 8. Infrom Users (NGO)
    
    ListOfWiners = NGO_Object.getWinnerList(AucId)
    
    print("\n")
    print("LIST OF WINNERS".center(TerminalSize,"-"))    

    print("\n")
    AucWinnerTitleString = " "*10 + "|  USER ID".ljust(UserDisplayWidth) + "|  WATTAGE (W)".ljust(UserDisplayWidth) + "|  PLEDGE START TIME".ljust(UserDisplayWidth)  + "|  PLEDGE DURATION (S)".ljust(UserDisplayWidth) + "|  INCENTIVE ASKED (TOKEN)".ljust(UserDisplayWidth)    
    print(AucWinnerTitleString)
    AucWinnerTitleString = " "*10 + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)  + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)    
    print(AucWinnerTitleString)
    
    count = 1
    for UserIdx in ListOfWiners:
        AucWinnerDisplayString = str("WINNER" + str(count)).ljust(10) +\
        str("|  " + UserIdx.user_id).ljust(UserDisplayWidth) +\
        str("|  " + str(UserIdx.Watt)).ljust(UserDisplayWidth) + \
        str("|  " + getstrtime(off_start)).ljust(UserDisplayWidth) + \
        str("|  " + str(UserIdx.UserOffDuration)).ljust(UserDisplayWidth) + \
        str("|  " + str(UserIdx.Incentive)).ljust(UserDisplayWidth) 
        
        print(AucWinnerDisplayString)
        print(AucWinnerTitleString)
        count = count+1
    
    #%% 9. Wait for TOff + DelT
    print("\n")
    print("WAITING FOR PLEDGE START".center(TerminalSize,"-")) 
    print("\n")
    OffPeridStart = True
    while OffPeridStart:
        currentTime = int(time.time())
        if currentTime < off_start:
    #        progress = int(bid_end - currentTime)
    #        if progress%10 == 0:
    #            sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    #            sys.stdout.flush()
            print("Pledge Perid starts in: {} seconds".format(int(off_start - currentTime)))
            
            time.sleep(4)
            for i in range(len(User_List)):
                UsgId = generateRandom("USG")
                # Get the device usage and pass to SC: Device are on State
                #%% Replace with actual Data --------------------------------------------
                User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
        else:
            OffPeridStart = False
            
    print("\n")
    print("PLEDGE PERIOD START".center(TerminalSize,"-")) 
            
    for UserIdx in User_List:
        UserIdx.Watt = 0
    
    User_List[1].Watt = 100
    
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
        #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    
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
            print("\nLogging Data from Devices!")
            print("Pledge Period ends in: {} seconds".format(int(off_end - currentTime)))
            for i in range(len(User_List)):
                UsgId = generateRandom("USG")
                # Get the device usage and pass to SC: Device are on State
                #%% Replace with actual Data --------------------------------------------
                if currentTime > off_start + User_List[i].UserOffDuration and User_List[i].Watt != User_List[i].RatedWatt:
                    User_List[i].Watt = User_List[i].RatedWatt
                    
                User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
                #if User_List[i].BidWin:
                    #print("User {} Consumption {} W".format(User_List[i].user_id,User_List[i].Watt))
                #%%-------------------------------------------------------------------------
            
            time.sleep(4)
        else:
            OffPeridEnd = False
    
    #%% ----------------------------------------------------------------------
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
        #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
                
    for WattIdx in range(len(User_List)):
        User_List[WattIdx].Watt = DeviceRated_Wattage[WattIdx]
        
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
        #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    
    print("\n")
    print("END OF PLEDGE PERIOD".center(TerminalSize,"-"))
    print("\nThank you for participating in the auction!")
    #%% -----------------------------------------------------------------------
    #Closing the auction
    NGO_Object.CloseAuctionPledge(AucId)
    
#    print("Smart Contract Intimated for closing the auction")
    
    # Logging data after auction
    for i in range(len(User_List)):
        UsgId = generateRandom("USG")
        # Get the device usage and pass to SC: Device are on State
    #%% Replace with actual Data --------------------------------------------
        User_List[i].logUsageData(Watt = User_List[i].Watt,UsgId = UsgId)
    #%%-------------------------------------------------------------------------
    
    #TO-DO display the total amount of energy saved
    #print("\n Off Period Ends! Thank you for saving Energy!") 
    time.sleep(1)       
    #%% 10. Settlement
    #TO-DO: Inform SC of end of OffPeriod and trigger settlement in SC
    
    print("\n")
    print("SETTLEMENT DETAILS".center(TerminalSize,"-")) 
    
    print("\n")
    PledgeWinnerTitleString = " "*10 + "|  USER ID".ljust(UserDisplayWidth) + "|  BID WIN".ljust(UserDisplayWidth) + "|  PLEDGE KEPT".ljust(UserDisplayWidth)  + "|  WALLET BALANCE (TOKEN)".ljust(UserDisplayWidth)   
    print(PledgeWinnerTitleString)
    PledgeWinnerTitleString = " "*10 + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth) + "|".ljust(UserDisplayWidth)  + "|".ljust(UserDisplayWidth)   
    print(PledgeWinnerTitleString)
    
    for UserIdx in User_List:
        
        UserIdx.showWalletBalance()
        
        DeviceData = UserIdx.getUsageData()
        for DataIdx in DeviceData:
                UserIdx.UpdateDataTime(DataIdx.timestamp)
                UserIdx.UpdateDataWatt(DataIdx.watt)
        
    for Idx in range(len(User_List)):
        #if PrevBal[Idx] == User_List[Idx].wallet_balance and User_List[Idx].BidWin:
            #print("User {} unsuccessful in completing contract!".format(User_List[Idx].user_id))
        if PrevBal[Idx] != User_List[Idx].wallet_balance and User_List[Idx].BidWin:
            #print("User {} successful in completing contract!".format(User_List[Idx].user_id))
            User_List[Idx].PledgeWin = True
    
    count1 = 0
    for UserIdx in User_List:
        PledgeDisplayString = str("USER" + str(count1)).ljust(10) +\
        str("|  " + UserIdx.user_id).ljust(UserDisplayWidth) +\
        str("|  " + str(UserIdx.BidWin).upper()).ljust(UserDisplayWidth) +\
        str("|  " + str(UserIdx.PledgeWin).upper()).ljust(UserDisplayWidth) +\
        str("|  " + str(UserIdx.wallet_balance)).ljust(UserDisplayWidth)
        count1 = count1 + 1
        print(PledgeDisplayString)
    
    api_instance = swagger_client.UserApi()
    user_id = NGO_Object.address # str |  (optional)
    
    try:
        api_response1 = api_instance.get_users(user_id=user_id)
        #pprint(api_response1)
    except ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
        
    WalletBalanceList = api_response1[0].wallet_balance
    NGO_Object.wallet_balance = WalletBalanceList
    #print("NGO Id: {}, Wallet: {}".format(NGO_Object.user_id,WalletBalanceList))
    print("\n")
    PledgeDisplayString = str("NGO").ljust(10) +\
        str("|  " + NGO_Object.user_id).ljust(UserDisplayWidth) +\
        str("|  ").ljust(UserDisplayWidth) +\
        str("|  ").ljust(UserDisplayWidth) +\
        str("|  " + str(NGO_Object.wallet_balance)).ljust(UserDisplayWidth)
    print(PledgeDisplayString)
        
    for UserIdx in User_List:
        UserIdx.UpdateDataAuction(offstart=off_start,offend = off_end)
            
    #Calculate KPIs for NGO
    NGO_Object.calculateKPI(User_List)
    
    # Reset BidWin and PledgeWin
    for UserIdx in User_List:
        UserIdx.BidWin = False
        UserIdx.PledgeWin = False
        
    print("\n")
    print("-".center(TerminalSize,"-")) 
#%%
#print("\nSettlement Details!")
#api_instance = swagger_client.UserApi()
#user_id = NGO_Object.address # str |  (optional)
#    
#try:
#    api_response1 = api_instance.get_users(user_id=user_id)
#    #pprint(api_response1)
#except ApiException as e:
#    print("Exception when calling UserApi->get_users: %s\n" % e)
#    
#WalletBalanceList = api_response1[0].wallet_balance
#    
#print("NGO Id: {}, Wallet: {}".format(NGO_Object.user_id,WalletBalanceList)) 
#    
#for UserIdx in Full_User_List:
#    user_id = UserIdx.address # str |  (optional)
#    
#    try:
#        api_response1 = api_instance.get_users(user_id=user_id)
#            #pprint(api_response1)
#    except ApiException as e:
#        print("Exception when calling UserApi->get_users: %s\n" % e)
#    
#    try:
#        WalletBalanceList = api_response1[0].wallet_balance
#    
#        print("USR Id: {}, Wallet: {}".format(UserIdx.user_id,WalletBalanceList))
#    except:
#        print("")
    
#%% Plotting results
Data_Time = [x - User_List[0].DataTime[0] for x in User_List[0].DataTime]
Data_Watt = User_List[0].DataWatt

trace1 = go.Scatter(
    x=Data_Time,
    y=Data_Watt
)

trace2 = go.Scatter(
    x=[40,40,100,100],
    y=[0,100,100,0],
    fill='tozeroy',
    fillcolor = '#e763fa',
    mode='none'
)


layout = dict(title = 'User 1 Consumption Profile',
              xaxis= dict(title= 'Time [s]'),
              yaxis= dict(title= 'Wattage [W]'),
             )

fig = go.Figure(data=[trace1,trace2],layout = layout)
plot(fig, filename='User1_Plot.html')

