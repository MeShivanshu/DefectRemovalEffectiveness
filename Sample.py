from itertools import count
import json
from re import T

from pkg_resources import Requirement
  
# Opening JSON file
with open('defects.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
#print(json_object)
#print(type(json_object))
#print("Requirements:",json_object["Field"])



######## VErtical Deefcts
totalVerticalRequirements = json_object["Requirements"][0]["Requirements"] + json_object["Requirements"][0]["Analysis"] + json_object["Requirements"][0]["Design"] + json_object["Requirements"][0]["Coding"] + json_object["Requirements"][0]["Unit Testing"] + json_object["Requirements"][0]["Integration Testing"] + json_object["Requirements"][0]["System Testing"] + json_object["Requirements"][0]["Field"]
#print(totalVerticalRequirements)
totalVerticalAnalysis = json_object["Analysis"][0]["Analysis"] + json_object["Analysis"][0]["Design"] + json_object["Analysis"][0]["Coding"] + json_object["Analysis"][0]["Unit Testing"] + json_object["Analysis"][0]["Integration Testing"] + json_object["Analysis"][0]["System Testing"] + json_object["Analysis"][0]["Field"]
#print(totalVerticalAnalysis)
totalVerticalDesign = json_object["Design"][0]["Analysis"] + json_object["Design"][0]["Design"] + json_object["Design"][0]["Coding"] + json_object["Design"][0]["Unit Testing"] + json_object["Design"][0]["Integration Testing"] + json_object["Design"][0]["System Testing"] + json_object["Design"][0]["Field"]
#print(totalVerticalDesign)
totalVerticalCoding = json_object["Coding"][0]["Analysis"] + json_object["Coding"][0]["Design"] + json_object["Coding"][0]["Coding"] + json_object["Coding"][0]["Unit Testing"] + json_object["Coding"][0]["Integration Testing"] + json_object["Coding"][0]["System Testing"] + json_object["Coding"][0]["Field"]
#print(totalVerticalCoding)
totalVerticalUnit = json_object["Unit Testing"][0]["Analysis"] + json_object["Unit Testing"][0]["Design"] + json_object["Unit Testing"][0]["Coding"] + json_object["Unit Testing"][0]["Unit Testing"] + json_object["Unit Testing"][0]["Integration Testing"] + json_object["Unit Testing"][0]["System Testing"] + json_object["Unit Testing"][0]["Field"]
#print(totalVerticalUnit)
totalVerticalIntegration = json_object["Integration Testing"][0]["Analysis"] + json_object["Integration Testing"][0]["Design"] + json_object["Integration Testing"][0]["Coding"] + json_object["Integration Testing"][0]["Unit Testing"] + json_object["Integration Testing"][0]["Integration Testing"] + json_object["Integration Testing"][0]["System Testing"] + json_object["Integration Testing"][0]["Field"]
#print(totalVerticalIntegration)
totalVerticalSystem = json_object["System Testing"][0]["Analysis"] + json_object["System Testing"][0]["Design"] + json_object["System Testing"][0]["Coding"] + json_object["System Testing"][0]["Unit Testing"] + json_object["System Testing"][0]["Integration Testing"] + json_object["System Testing"][0]["System Testing"] + json_object["System Testing"][0]["Field"]
#print(totalVerticalSystem)
totalVerticalField = json_object["Field"][0]["Analysis"] + json_object["Field"][0]["Design"] + json_object["Field"][0]["Coding"] + json_object["Field"][0]["Unit Testing"] + json_object["Field"][0]["Integration Testing"] + json_object["Field"][0]["System Testing"] + json_object["Field"][0]["Field"]
#print(totalVerticalField)


##### HORizontal Defectas
totalHorizontalRequirements = json_object["Requirements"][0]["Requirements"] + json_object["Analysis"][0]["Requirements"] + json_object["Design"][0]["Requirements"] + json_object["Coding"][0]["Requirements"] + json_object["Unit Testing"][0]["Requirements"] + json_object["System Testing"][0]["Requirements"] + json_object["Integration Testing"][0]["Requirements"] + json_object["Field"][0]["Requirements"]
#print(totalHorizontalRequirements)
totalHorizontalAnalysis = json_object["Requirements"][0]["Analysis"] + json_object["Analysis"][0]["Analysis"] + json_object["Design"][0]["Analysis"] + json_object["Coding"][0]["Analysis"] + json_object["Unit Testing"][0]["Analysis"] + json_object["System Testing"][0]["Analysis"] + json_object["Integration Testing"][0]["Analysis"] + json_object["Field"][0]["Analysis"]
#print(totalHorizontalAnalysis)
totalHorizontalDesign = json_object["Requirements"][0]["Design"] + json_object["Analysis"][0]["Design"] + json_object["Design"][0]["Design"] + json_object["Coding"][0]["Design"] + json_object["Unit Testing"][0]["Design"] + json_object["System Testing"][0]["Design"] + json_object["Integration Testing"][0]["Design"] + json_object["Field"][0]["Design"]
#print(totalHorizontalDesign)
totalHorizontalCoding = json_object["Requirements"][0]["Coding"] + json_object["Analysis"][0]["Coding"] + json_object["Design"][0]["Coding"] + json_object["Coding"][0]["Coding"] + json_object["Unit Testing"][0]["Coding"] + json_object["System Testing"][0]["Coding"] + json_object["Integration Testing"][0]["Coding"] + json_object["Field"][0]["Coding"]
#print(totalHorizontalCoding)
totalHorizontalUnit = json_object["Requirements"][0]["Unit Testing"] + json_object["Analysis"][0]["Unit Testing"] + json_object["Design"][0]["Unit Testing"] + json_object["Coding"][0]["Unit Testing"] + json_object["Unit Testing"][0]["Unit Testing"] + json_object["System Testing"][0]["Unit Testing"] + json_object["Integration Testing"][0]["Unit Testing"] + json_object["Field"][0]["Unit Testing"]
#print(totalHorizontalUnit)
totalHorizontalIntegration = json_object["Requirements"][0]["Integration Testing"] + json_object["Analysis"][0]["Integration Testing"] + json_object["Design"][0]["Integration Testing"] + json_object["Coding"][0]["Integration Testing"] + json_object["Unit Testing"][0]["Integration Testing"] + json_object["System Testing"][0]["Integration Testing"] + json_object["Integration Testing"][0]["Integration Testing"] + json_object["Field"][0]["Integration Testing"]
#print(totalHorizontalIntegration)
totalHorizontalSystem = json_object["Requirements"][0]["System Testing"] + json_object["Analysis"][0]["System Testing"] + json_object["Design"][0]["System Testing"] + json_object["Coding"][0]["System Testing"] + json_object["Unit Testing"][0]["System Testing"] + json_object["System Testing"][0]["System Testing"] + json_object["Integration Testing"][0]["System Testing"] + json_object["Field"][0]["System Testing"]
#print(totalHorizontalSystem)
totalHorizontalField = json_object["Requirements"][0]["Field"] + json_object["Analysis"][0]["Field"] + json_object["Design"][0]["Field"] + json_object["Coding"][0]["Field"] + json_object["Unit Testing"][0]["Field"] + json_object["System Testing"][0]["Field"] + json_object["Integration Testing"][0]["Field"] + json_object["Field"][0]["Field"]
#print(totalHorizontalField)


############ TOTAL DEFECTS#####
grandtotalVertical = totalVerticalRequirements + totalVerticalSystem + totalVerticalAnalysis + totalVerticalCoding + totalVerticalIntegration + totalVerticalDesign + totalVerticalUnit + totalVerticalField
#print(grandtotalVertical)
grandtotalHorizontal = totalHorizontalRequirements + totalHorizontalSystem + totalHorizontalAnalysis + totalHorizontalCoding + totalHorizontalIntegration + totalHorizontalDesign + totalHorizontalUnit + totalHorizontalField
#print(grandtotalHorizontal)

################ Finding Injection and Exit
RequirementsEntry = 0
RequirementsExit = totalVerticalRequirements - totalHorizontalRequirements
#print("          ",RequirementsEntry,RequirementsExit)


AnalysisEntry = RequirementsExit
AnalysisExit = AnalysisEntry + totalVerticalAnalysis - totalHorizontalAnalysis 
#print(AnalysisExit)


DesignEntry = AnalysisExit
DesignExit = DesignEntry + totalVerticalDesign - totalHorizontalDesign
#print(DesignExit)


CodingEntry = DesignExit
CodingExit = CodingEntry + totalVerticalCoding - totalHorizontalCoding
#print(CodingExit)


UnitEntry = CodingExit
UnitExit =  UnitEntry + totalVerticalUnit - totalHorizontalUnit
#print(UnitExit)


IntEntry = UnitExit
IntExit = IntEntry + totalVerticalIntegration - totalHorizontalIntegration
#print(IntExit)



SystemEntry = IntExit
SystemExit =  SystemEntry + totalVerticalSystem - totalHorizontalSystem
#print(SystemExit)


FieldEntry = SystemExit
FieldExit = FieldEntry + totalVerticalField - totalHorizontalField
#print(FieldExit)

##########  Defect Removal Effectiveness

RequirementsDRE = (totalHorizontalRequirements)/(RequirementsEntry + totalVerticalRequirements)*100

AnalysisDRE = (totalHorizontalAnalysis)/(AnalysisEntry + totalVerticalAnalysis)*100

DesignDRE = (totalHorizontalDesign)/(DesignEntry + totalVerticalDesign)*100

CodingDRE = (totalHorizontalCoding)/(CodingEntry + totalVerticalCoding)*100

UnitDRE = (totalHorizontalUnit)/(UnitEntry + totalVerticalUnit)*100

IntegrationDRE = (totalHorizontalIntegration)/(IntEntry + totalVerticalIntegration)*100

SystemDRE = (totalHorizontalSystem)/(SystemEntry + totalVerticalSystem)*100

FieldDRE = (totalHorizontalField)/(FieldEntry + totalVerticalField)*100

UnitDRE2 = (totalHorizontalUnit)/(totalHorizontalUnit + totalHorizontalIntegration + totalHorizontalSystem +totalHorizontalField)*100

IntegrationDRE2 = (totalHorizontalIntegration)/( totalHorizontalIntegration + totalHorizontalSystem +totalHorizontalField)*100

SystemDRE2 = (totalHorizontalSystem)/(totalHorizontalSystem +totalHorizontalField)*100

FieldDRE2 = (totalHorizontalField)/(totalHorizontalField)*100
######## Calculating Phase details
print("PHASE-WISE DETAILS OF DEFECTS:")
print(f"""

For Inspection Phase, we use the following formula for finding Defect Removal Effectiveness :
        (Defects removed at current phase)/(Defects existing at phase entry + Defects injected during development of phase)

However, for Testing phases we use the DUnn's Formula for finding DRE :
        (Defects Removed at current phase)/(Defects removed at current phase + Defects removed at subsequent steps)
------------Phase 1 :   Requirements-----------
Defect Entry Rate : {RequirementsEntry}
Defect Injection Rate : {totalVerticalRequirements}
Defect Removal Rate : {totalHorizontalRequirements}
Effective Removal Effectiveness : {RequirementsDRE}
Defects Exited : {RequirementsExit}
------------Phase 2 :   Analysis-----------
Defect Entry Rate : {AnalysisEntry}
Defect Injection Rate : {totalVerticalAnalysis}
Defect Removal Rate : {totalHorizontalAnalysis}
Effective Removal Effectiveness : {AnalysisDRE}
Defects Exited : {AnalysisExit}
------------Phase 3 :   Design-----------
Defect Entry Rate : {DesignEntry}
Defect Injection Rate : {totalVerticalDesign}
Defect Removal Rate : {totalHorizontalDesign}
Effective Removal Effectiveness : {DesignDRE}
Defects Exited : {DesignExit}
------------Phase 4 :   Coding-----------
Defect Entry Rate : {CodingEntry}
Defect Injection Rate : {totalVerticalCoding}
Defect Removal Rate : {totalHorizontalCoding}
Effective Removal Effectiveness : {CodingDRE}
Defects Exited : {CodingExit}
------------Phase 5 :   Unit Testing-----------
Defect Entry Rate : {UnitEntry}
Defect Injection Rate : {totalVerticalUnit}
Defect Removal Rate : {totalHorizontalUnit}
Effective Removal Effectiveness : Using normal formula {UnitDRE}
                                  Using DUnn's formula {UnitDRE2}
Defects Exited : {UnitExit}
------------Phase 6 :   Integration Testing-----------
Defect Entry Rate : {IntEntry}
Defect Injection Rate : {totalVerticalIntegration}
Defect Removal Rate : {totalHorizontalIntegration}
Effective Removal Effectiveness : Using normal formula :{IntegrationDRE}
                                  Using DUnn's FOrmula : {IntegrationDRE2}
Defects Exited : {IntExit}
------------Phase 7 :   System Testing-----------
Defect Entry Rate : {SystemEntry}
Defect Injection Rate : {totalVerticalSystem}
Defect Removal Rate : {totalHorizontalSystem}
Effective Removal Effectiveness : Using normal formula :{SystemDRE}
                                  Using Dunn's Formula :{SystemDRE2}
Defects Exited : {SystemExit}
------------Phase 8 :   Field-----------
Defect Entry Rate : {FieldEntry}
Defect Injection Rate : {totalVerticalField}
Defect Removal Rate : {totalHorizontalField}
Effective Removal Effectiveness : {FieldDRE}
Defects Exited : {FieldExit}
""")