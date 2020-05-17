#Capital Gains Tax (CGT) - Individuals
#CGT is payable by individuals on thier taxable gains.
#If there is an increase in value on disposal, there is a chargeable gain (a fall in value results in an allowable loss).
#Chargeable disposals include sale, gift or loss/destruction of an asset or part of an asset.
#Exempt disposals include gifts to charties.
#There is no CGT on death (but those who receive the asset get it at its market rate value at the time of death, which can result in a tax free uplift).
#Chargeable assets include land, furniture, art, goodwill, shares and leases.
#Exempt assets include cash, cars, wasting chattels, chattels (where acquisition cost and gross disposal consideration less than or equal to £6000),
#and gilt-edged securities (e.g. Treasury stock), National Savings Certificates, investments held in ISAs.

#Calculating a gain or loss
disposalConsideration = 0 #Sales proceeds (if sold) or market value (if gifted)
incidentalCostsOfDisposal = 0 #e.g. legal fees, estate agent's fees, advertising costs
netDisposalConsideration = disposalConsideration - incidentalCostsOfDisposal
allowableCosts = 0 #Acquisition costs, incidental costs of acquistions (e.g. stamp duty), enchancement capital expenditure (e.g. additions and improvements)
chargeableGainOrLoss = netDisposalConsideration - allowableCosts
print(f"Chargeable gain or allowable loss on disposal of chargeable asset is £{chargeableGainOrLoss}")

#Chattels - special rules apply to chattels
#Chattels are tangible moveable property.
#Wasting chattels are chattels with a predictable life of 50 years or less (e.g. computers, plant and machinery)
#Non-wasting chattels are chattels with predictable life of more than 50 years (e.g. antiques)
chattelAcquisitionCost = 15000
chattelProceeds = 40000
chattelCostsOfSale = 2000
chargeableGainOnChattel = 0
wastingChattel = False
nonwastingChattel = False
lifeAtDisposal = 51 #years
if lifeAtDisposal <= 50:
    wastingChattel = True
else:
    nonwastingChattel = True
if wastingChattel == True:
    chargeableGainOnChattel = 0
elif nonwastingChattel == True:
    if chattelAcquisitionCost <= 6000 and chattelProceeds <= 6000:
        chargeableGainOnChattel = 0
    elif chattelAcquisitionCost <= 6000 and chattelProceeds > 6000:
        cannotExceed = 5/3 * (chattelProceeds - 6000)
        chargeableGainOnChattel = chattelProceeds - chattelCostsOfSale - chattelAcquisitionCost
        if chargeableGainOnChattel > cannotExceed:
            chargeableGainOnChattel = cannotExceed
        else:
            chargeableGainOnChattel = chargeableGainOnChattel
    elif chattelProceeds < 6000 and chattelAcquisitionCost > chattelProceeds: #Would result in a loss, so assume proceeds were 6000
        chattelProceeds = 6000
        chargeableGainOnChattel = chattelProceeds - chattelCostsOfSale - chattelAcquisitionCost
        if chargeableGainOnChattel > 0:
            chargeableGainOnChattel = 0
    else:
        chargeableGainOnChattel = chattelProceeds - chattelCostsOfSale - chattelAcquisitionCost
print(f"Chargeable gain or allowable loss on disposal of chattel is £{round(chargeableGainOnChattel)}")

#Calculating CGT payable
annualExemptAmount = 11700 #tax year 2018/19
taxableGains = chargeableGainOrLoss + chargeableGainOnChattel - annualExemptAmount
taxableIncome = 0
basicRateCeiling = 34500 #tax year 2018/19
basicCGTRate = 0.1
higherCGTRate = 0.2
#Calculate CGT liable
liableCGT = 0
if taxableIncome + taxableGains <= basicRateCeiling:
    liableCGT = taxableGains * basicCGTRate
elif taxableIncome > basicRateCeiling:
    liableCGT = taxableGains * higherCGTRate
elif taxableIncome <= basicRateCeiling and (taxableIncome + taxableGains) > basicRateCeiling:
    liableCGT = (basicRateCeiling - taxableIncome) * basicCGTRate + (taxableGains - (basicRateCeiling - taxableIncome)) * higherCGTRate
print(f"Capital gains tax liability is £{liableCGT}")

