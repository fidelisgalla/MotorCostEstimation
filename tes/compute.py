#computation of model
import requests
from forex_python.converter import CurrencyRates
import datetime
from response import copperPrice,aluminiumPrice,steelPrice
class CalculationMotorPrice:
    def __init__(self):
        self.base_currency ='USD'
        self.endpoint = 'latest'
        self.access_key = 'lmsv4mftmwzpto2jc0q2xsj20613dxdrb14fp6y1u2lk65fh75tkzp0p6rbm'
        self.symbols = 'LME-XCU,LME-ALU,STEEL-HR'

    def getMetalsPrice(self):
        resp = requests.get('https://metals-api.com/api/'+self.endpoint+'?access_key=' +
                            self.access_key+ '&base=' +self.base_currency + '&symbols=' +self.symbols)
        if resp.status_code !=200:
            raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))
        resp = resp.json()
        priceCopper = resp['rates']['LME-XCU']
        priceAluminum = resp['rates']['LME-ALU']
        priceSteel = resp['rates']['STEEL-HR']
        return priceCopper, priceAluminum, priceSteel

    def getUSDIDRRate(self):
        c = CurrencyRates()
        kursRupiah = c.get_rate('USD','IDR')
        return kursRupiah

    def inflasiCalculation(self,years):
        inflasi2010 = 0.0696
        inflasi2011 = 0.0379
        inflasi2012 = 0.0430
        inflasi2013 = 0.0838
        inflasi2014 = 0.0836
        inflasi2015 = 0.0335
        inflasi2016 = 0.0302
        inflasi2017 = 0.0361
        inflasi2018 = 0.0313
        inflasi2019 = 0.0272
        inflasi2020 = 0.0168
        inflasi2021 = 0.0187

        if years == 2010:
            inflation2010 = 1+inflasi2010
            return inflation2010
        elif years == 2011:
            inflation2011 = 1+inflasi2011*(1+inflasi2010)
            return inflation2011
        elif years == 2012:
            inflation2012 = 1+inflasi2012*(1+inflasi2011*(1+inflasi2010))
            return inflation2012
        elif years == 2013:
            inflation2013 = 1+inflasi2013*(1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010)))
            return inflation2013
        elif years == 2014:
            inflation2014 = 1+inflasi2014*(1 + inflasi2013 * (1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010))))
            return inflation2014
        elif years == 2015:
            inflation2015 = 1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 * (1 + inflasi2012 *
                                                                             (1 + inflasi2011 * (1 + inflasi2010)))))
            return inflation2015
        elif years == 2016:
            inflation2016 = 1+inflasi2016*(1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 *(1 + inflasi2012 *
                                                                                           (1 + inflasi2011 * (1 + inflasi2010))))))
            return inflation2016
        elif years == 2017:
            inflation2017 = 1+inflasi2017*(1+inflasi2016*(1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 *
                                                                                        (1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010)))))))
            return inflation2017
        elif years == 2018:
            inflation2018 = 1+inflasi2018*(1+inflasi2017*(1+inflasi2016*(1+inflasi2015*(1+inflasi2014*
                                                                                        (1 + inflasi2013 *(1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010))))))))
            return inflation2018
        elif years == 2019:
            inflation2019 = 1+inflasi2019*(1+inflasi2018*(1+inflasi2017*
                                                          (1+inflasi2016*(1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 *(1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010)))))))))
            return inflation2019
        elif years ==2020:
            inflation2020 = 1+inflasi2020*(1+inflasi2019*(1+inflasi2018*(1+inflasi2017*
                                                                         (1+inflasi2016*(1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 *(1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010))))))))))
            return inflation2020
        elif years == 2021:
            inflation2021 = 1+inflasi2021*(1+inflasi2020*(1+inflasi2019*(1+inflasi2018*
                                                                         (1+inflasi2017*(1+inflasi2016*(1+inflasi2015*(1+inflasi2014*(1 + inflasi2013 *(1 + inflasi2012 * (1 + inflasi2011 * (1 + inflasi2010)))))))))))
            return inflation2021
        else:
            return 'Error Years'

    def percentageCapacityFactor(self,knownMotorCapacity,requestedMotorCapacity):
        capFactor = (requestedMotorCapacity/knownMotorCapacity) ** 0.75 #this formula refer DOE
        return capFactor

    def percentageSteelComponent(self,priceSteelWhenBought):

        #priceSteelWhenBought = 0.015523476744334  # please check (per ounce)
        #priceSteelToday = self.getMetalsPrice()[2]
        priceSteelToday = steelPrice()
        increasedFactorSteel = (priceSteelToday - priceSteelWhenBought) / priceSteelToday
        return increasedFactorSteel

    def percentageCopperComponent(self,priceCopperWhenBought):

        #priceCopperWhenBought = 0.22444214278383  # in USD/lbs
        #priceCopperToday = self.getMetalsPrice()[0]
        priceCopperToday = copperPrice()
        increasedFactorCopper = (priceCopperToday - priceCopperWhenBought) / priceCopperToday
        return increasedFactorCopper

    def percentageAluminiumComponent(self,priceAlumniumWhenBought):

        #priceAlumniumWhenBought = 0.060758804629448  # in USD/T
        #priceAlumniumToday = self.getMetalsPrice()[1]
        priceAlumniumToday = aluminiumPrice()
        increasedFactorAluminium = (priceAlumniumToday - priceAlumniumWhenBought) / priceAlumniumToday
        return increasedFactorAluminium

    def computeMotorMediumVoltage(self,motorVoltage,motorCapacity):
        if motorVoltage == '3300 V':
            steelComponentPercentage = 0.4762
            copperComponentPercentage = 0.1257
            alumniumComponentPercentage = 0.1720

        #REFERENSI 1
            knownMotorCap = 510
            knownMotorPrice = 1390000000 #in IDR
            yearsBoughtRef1 = 2020
            priceCopRef1 = 6.489
            priceAluRef1 = 1.68
            priceSteelRef1 = 0.5228

            percentageCapacityFactorRef1 = self.percentageCapacityFactor(knownMotorCap,motorCapacity)
            percentageCopperComponentRef1 = self.percentageCopperComponent(priceCopRef1)*copperComponentPercentage
            percentageSteelComponentRef1 = self.percentageSteelComponent(priceSteelRef1)*steelComponentPercentage
            percentageAluminiumComponentRef1 = self.percentageAluminiumComponent(priceAluRef1)*alumniumComponentPercentage
            inflasiRate = self.inflasiCalculation(yearsBoughtRef1)-1

            priceRef1 = knownMotorPrice*(percentageCapacityFactorRef1)*(1+percentageCopperComponentRef1)*(1+percentageSteelComponentRef1)*\
                    (1+percentageAluminiumComponentRef1)*(1+inflasiRate)

        #referensi 2
            knownMotorCapRef2 = 415
            knownMotorPriceRef2 = 910000000
            yearsBoughtRef2 = 2017
            priceCopRef2 = 6.873
            priceAluRef2 = 1.735
            priceSteelRef2 = 0.689

            percentageCapacityFactorRef2 = self.percentageCapacityFactor(knownMotorCapRef2,motorCapacity)
            percentageCopperComponentRef2 = self.percentageCopperComponent(priceCopRef2)*copperComponentPercentage
            percentageSteelComponentRef2 = self.percentageSteelComponent(priceSteelRef2)*steelComponentPercentage
            percentageAluminiumComponentRef2 = self.percentageAluminiumComponent(priceAluRef2)*alumniumComponentPercentage
            inflasiRateRef2 = self.inflasiCalculation(yearsBoughtRef2) - 1

            priceRef2 = knownMotorPriceRef2 * (percentageCapacityFactorRef2) * (1 + percentageCopperComponentRef2) * \
                    (1 + percentageSteelComponentRef2) *(1 + percentageAluminiumComponentRef2) * (1 + inflasiRateRef2)

        # referensi 3
            knownMotorCapRef3 = 600
            knownMotorPriceRef3 = 1905000000
            yearsBoughtRef3 = 2021
            priceCopRef3 = 9.667
            priceAluRef3 = 3.18
            priceSteelRef3 = 0.97

            percentageCapacityFactorRef3 = self.percentageCapacityFactor(knownMotorCapRef3, motorCapacity)
            percentageCopperComponentRef3 = self.percentageCopperComponent(priceCopRef3)*copperComponentPercentage
            percentageSteelComponentRef3 = self.percentageSteelComponent(priceSteelRef3)*steelComponentPercentage
            percentageAluminiumComponentRef3 = self.percentageAluminiumComponent(priceAluRef3)*alumniumComponentPercentage
            inflasiRateRef3 = self.inflasiCalculation(yearsBoughtRef3)-1


            priceRef3 = knownMotorPriceRef3 * (percentageCapacityFactorRef3) * (1 + percentageCopperComponentRef3) * \
                    (1 + percentageSteelComponentRef3) * (1 + percentageAluminiumComponentRef3) * (1 + inflasiRateRef3)

            result = (priceRef1+priceRef2+priceRef3)/3

            return 'Harga motor kapasitas {} kW'.format(motorCapacity)+' adalah Rp{:,.2f}'.format(result)+' dengan details harga Copper (USD/T) adalah Rp {:,.2f}.'.format(copperPrice())+' harga Aluminium Rp {:,.2f}'.format(alumniumComponentPercentage)+\
                   ' harga Steel Rp {:,.2f}'.format(steelPrice())

        elif motorVoltage == '380 V':
            return 'nanti aja'
