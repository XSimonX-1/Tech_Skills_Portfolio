EN:
Task: Testing Methods with SoapUI

You are given a project within your company that needs to be tested using SoapUI.

The interface provides database access to various data about countries.

WSDL file to load: http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL

Your task is to automate the testing of the application.

1: Creating the Project

	•	Based on the above WSDL, create a new Soap project named Vizsga_Country_Info.

2: Creating the Tests

	•	Create a TestSuite named Info_About_Countries, which contains a TestCase called France. The TestCase should include the CountryISOCode and CapitalCity requests.

3: Creating Assertions

	•	In the TestCase, both requests should have a filled-in Response SLA, a Valid HTTP Status Codes, and an XPath Match assertion, in addition to the basic Soap Response.

4: Externalizing and Using Test Data

	•	Create a Properties TestStep named TestData, where you will save the country name, ISOCode, and capital city.
	•	Use this data in the request sections of the CountryISOCode and CapitalCity TestSteps, and also use it to fill in the expected results for the XPath Match assertions.




HU:
Feladat: Metódusok tesztelése SoapUI segítségével

Adott egy projekt a cégen belül, ahol dolgoztok, amit SoapUI segítségével kell letesztelni.

Az interface országok különféle adataihoz ad adatbázis hozzáférést. 

Betöltendő WSDL állomány: [http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL](http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL)

Feladatod, hogy automatizáld az alkalmazás tesztelését.

## 1: Projekt létrehozás
* A fenti WSDL alapján hozz létre egy új Soap projektet, aminek a neve legyen `Vizsga_Country_Info`.

## 2: Tesztek létrehozása
* Hozz létre egy TestSuite-ot `Info_About_Countries` néven, ami tartalmaz egy `France` nevezetű TestCase-t. A TestCase tartalmazza a `CountryISOCode` és a `CapitalCity` requesteket.

## 3: Assertek létrehozása
* A TestCase-ben mindkét request tartalmazzon kitöltve egy `Response SLA`, egy `Valid HTTP Status Codes`, és egy `XPath Match` assertet az alap Soap Response-on felül.

## 4: Tesztadatok kiszervezése és felhasználása
* Készíts egy `Properties TestStep`-et, TestData néven, ahová mentsd el az országnevet, az ISOCode-ot, és a fővárost is.
* Ezeket az adatokat használd fel a CountryISOCode és a CapitalCity TestStepek request oldalán, illetve az Xpath Match-ek elvárt eredményét is ezek segítségével töltsd ki.
