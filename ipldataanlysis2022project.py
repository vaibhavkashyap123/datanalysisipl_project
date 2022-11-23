import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sw
import numpy as np
player_price=pd.read_csv('data/player_price_2022.csv')
print(player_price)
# for find the shape of the dataset
print(player_price.shape)
# info and datatype of the dataset
print(player_price.info())
# for the columns in the dataset
col=player_price.columns
print(col)
# drop useless column in the dataset
player_price.drop('Unnamed: 0',axis=1,inplace=True)
top=player_price.head(5)
print(top)
# to set index on dataset
player_price.set_index('Player')
#for finding the
null=player_price.isnull().sum()
print(null)
# for finding null
null=player_price[player_price['COST IN ₹ (CR.)'].isnull()]
player_price['COST IN ₹ (CR.)']=player_price['COST IN ₹ (CR.)'].fillna(0)
player_price['Cost IN $ (000)']=player_price['Cost IN $ (000)'].fillna(0)
player_unsold=player_price[player_price['2021 Squad'].isnull()]
player_price['2021 Squad']=player_price['2021 Squad'].fillna('Not Participated')
nos=player_price[player_price['2021 Squad']=='Not Participated']
print(nos)
#means no null values in the dataset
print(player_price.isnull().sum())
#team where cost is greater than 0
Teams=player_price[player_price['COST IN ₹ (CR.)']>0]['Team'].unique()
print(Teams)
#player_price['status']=player_price['Team'].replace('Sold')
#print(player_price.head(4))
#player_price.drop('status',axis=1,inplace=True)
'''heads=player_price.head(5)
print(heads)
print(player_price.columns)'''
player_price['Status']=player_price['Team'].replace(Teams,'Sold')
print(player_price.head(5))
a=player_price[player_price['Player'].duplicated(keep=False)]
print(a)
# how many players sold in 2022 ipl auction
# player_price[player_price['Status']=='Unsold'].to_csv('unsold.csv',index=False)
Unsold_players=pd.read_csv('unsold.csv')
# print(Unsold_players)
# how many participated
participation=player_price.shape[0]
print(participation)
# how many types of players participated
type=player_price['TYPE'].value_counts()
type.reset_index()
print(type)
#for pie chart
plt.pie(type.values,labels=type.index,labeldistance=1.2,autopct='%1.2f%%',startangle=60)
plt.title('Number of Players Participated',fontsize=20)
plt.show()
print(player_price.columns)
# bar chart
plt.figure(figsize=(20,28))
fig=sw.countplot(data=player_price,x='Status',palette=['Orange','Yellow'])
plt.xlabel('Sold Vs Unsold')
plt.ylabel('Number Of Players')
plt.title('The Sold Unsold Players')
plt.show()
# to check the bar graph
p=player_price.groupby('Status')['Player'].count()
print(p)
#a=player_price[player_price['Team']!='Unsold'].to_csv('Sold.csv')
sold_players=pd.read_csv('Sold.csv')
#c=sold_players.groupby('Team').count()
#retentition base price and base price unit column are made upto
#a=sold_players.groupby('Team').count()
#print(a['Player'])
#sw.countplot(data=a,x=a['Player'],hue='Team')
#plt.show()
sold_players['retention']=sold_players['Base Price']
print(sold_players.columns)
print(sold_players['retention'].unique())
sold_players['retention']=sold_players['retention'].replace(['2 Cr','40 Lakh','20 Lakh','1 Cr','75 Lakh','50 Lakh','30 Lakh','1.5 Cr'],'From Auction')
print(sold_players)
sold_players['Base Price'].replace('Draft Pick',0,inplace=True)
sold_players['Base_Price_unit']=sold_players['Base Price'].apply(lambda x:str(x).split(' ')[-1])
#print(player_price.columns)
sold_players['BasePrice']=sold_players['Base Price'].apply(lambda x:str(x).split(' ')[0])
print(sold_players['BasePrice'])
print(sold_players['Base_Price_unit'])
sold_players['BasePrice'].replace('retained',0,inplace=True)
print(sold_players['BasePrice'])
#how many players retained and bought from each teams
#sold_players.to_csv('sold_players_edit.csv')
solds=pd.read_csv('sold_players_edit.csv')
x=solds.groupby(['Team','retention'])['retention'].count()
#retained players from teams
retained=solds[solds['retention']=='Retained'][['Player','Team']]
print(retained)
#sold players me se kis type ke players the diffrent team me
sw.countplot(x='Team',hue='TYPE',data=sold_players)
plt.xticks(rotation=35,fontsize=8)
plt.xlabel('Teams')
plt.ylabel('Count of players of diffrent Types')
plt.title('Count of players of diffrent types in diffrent Teams')
plt.show()
# Maximum Amount of payed(In Auction) by each team for an player
max_amount_by_teams_in_auction=solds[solds['retention']=='From Auction'].groupby('Team')[['COST IN ₹ (CR.)','Player']].max()
print(max_amount_by_teams_in_auction)
# Max Amount of payed(In retention) by each team for an player
max_amount_of_teams_in_retention=solds[solds['retention']=='Retained'].groupby('Team')[['COST IN ₹ (CR.)','Player']].max()
print(max_amount_of_teams_in_retention)
retention_top=solds[solds['retention']=='Retained'].sort_values(by='COST IN ₹ (CR.)',ascending=False)[['Player','Team','COST IN ₹ (CR.)']].head(1)
print(retention_top)
top_five_bowlers=solds[(solds['retention']=='From Auction') & (solds['TYPE']=='BOWLER')].sort_values(by='COST IN ₹ (CR.)',ascending=False)[['Player','Team','COST IN ₹ (CR.)']].head(5)
print(top_five_bowlers)
#top 10 batsman by amount payed
top_ten_batters=solds[(solds['retention']=='From Auction') & (solds['TYPE']=='BATTER')].sort_values(by='COST IN ₹ (CR.)',ascending=False)[['Player','Team','COST IN ₹ (CR.)']].head(10)
print(top_ten_batters)
solds.rename(columns={'2021 Squad':'Previous Team'})
print(solds)
#solds.to_csv('Sold_players_data_analysis_csvfile.csv')
