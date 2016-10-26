import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement, Element
import csv
import codecs

def csv_row_to_mods(dest,number):
    """csv_row->List(String) a single row read in from a csv reader
       csv_defs->List(String) the first row from a csv file to give the dict keys
       dest->(String) Path to folder where MODS.xml will be saved
       date->(Stirng) DateCaptured YYYY-MM-DD from scandata

       the following keys are currently in use:
        title
        role
        dateCaptured
        dateQualifier
        dateCreated
        noteOnDateCreated
        description
        identifierLocal
        form
        extent
        note
        language
        topic
        continent
        country
        province
        state
        county
        city
        coordinates
        source

        The keys from the csv file are checked to exist before setting the data, because some meta data won't always be there.
        
        Create a mods file from a csv row (already processed in lists) """

    xmlns_uris = ['http://www.loc.gov/mods/v3', 'http://www.loc.gov/mods/v3','http://www.w3.org/2001/XMLSchema-instance','http://www.w3.org/1999/xlink']
    
    mods = Element("mods")
    mods.attrib['xmlns'] = xmlns_uris[0]
    mods.attrib['xmlns:mods'] = xmlns_uris[1]
    mods.attrib['xmlns:xsi'] = xmlns_uris[2]
    mods.attrib['xmlns:xlink'] = xmlns_uris[3]

    titleinfo = SubElement(mods,'titleInfo')
    title = SubElement(titleinfo,'title')
    title.text = number


    name = SubElement(mods,'name')
    name.attrib['type'] = "personal" # Hardcoded
    namepartname = SubElement(name,'namePart')
    namepartname.text = "Spiller, Harley J."
    namepartdate = SubElement(name,'namePart')
    namepartdate.attrib['type']='date'
    namepartdate.text = "1959-"

    role = SubElement(name,'role')
    rolepart = SubElement(role,'roleTerm')
    rolepart.text = ""
    rolepart.attrib['authority'] = "marcrelator"
    rolepart.attrib['type'] = "text"

    typeofresource= SubElement(mods,'typeOfResource')
    typeofresource.text = "text"

    genre = SubElement(mods,'genre')
    genre.text = "menu"

    origininfo = SubElement(mods,'originInfo')
    datecaptured = SubElement(origininfo,'dateCaptured')
    datecaptured.text = ""
    datecreated = SubElement(origininfo, 'dateCreated')
    datecreated.attrib['qualifier'] = ""
    datecreated.text = ""

    datenote = SubElement(mods,'note')
    datenote.attrib['ID'] = "datenote"
    datenote.text = ""

    description = SubElement(mods,'abstract')
    description.text = ""

    identifier= SubElement(mods,'identifier')
    identifier.attrib['type'] = "local"
    identifier.text = ""


    physicaldesc = SubElement(mods,'physicalDescription')
    form = SubElement(physicaldesc,'form')
    form.attrib['authority'] = "marcform"
    form.text = ""
    extent = SubElement(physicaldesc,'extent')
    extent.text = ""

    note = SubElement(mods,'note')
    note.text = ""

    language = SubElement(mods,'language')
    languageterm = SubElement(mods,'languageTerm')
    languageterm.attrib['authority'] = "iso639-2b"
    languageterm.attrib['type'] = "code"
    language.text = ""

    subject = SubElement(mods,'subject')
    topic = SubElement(subject,'topic')
    topic.attrib['authority'] = "lcsh"
    topic.text = ""

    geographic = SubElement(subject,'geographic') # TODO blank?
    temporal = SubElement(subject,'temporal') # TODO blank?
    hierarchicalgeographic = SubElement(subject,'hierarchicalGeographic')
    continent = SubElement(hierarchicalgeographic,'continent')
    continent.text = ""
    country = SubElement(hierarchicalgeographic,'country')
    country.text = ""
    province = SubElement(hierarchicalgeographic,'province')
    province.text = ""
    state = SubElement(hierarchicalgeographic,'state')
    state.text = ""
    region = SubElement(hierarchicalgeographic,'region') 
    county = SubElement(hierarchicalgeographic,'county') 
    county.text = ""
    city = SubElement(hierarchicalgeographic,'city') 
    city.text = ""
    citysection= SubElement(hierarchicalgeographic,'citySection') 
    cartographics = SubElement(subject,'cartographics')
    coordinates = SubElement(cartographics,'coordinates')
    coordinates.text = ""


    location = SubElement(mods,'location')
    holdinginstitution = SubElement(location,'physicalLocation')
    holdinginstitution.attrib['type'] = "holdingInstitution"
    holdinginstitution.text = "University of Toronto Scarborough Library, Archives & Special Collections"
    source = SubElement(location,'physicalLocation')
    source.attrib['type'] = "source"
    source.text = ""
    
    accesscondition = SubElement(mods,'accessCondition') # Rights
    accesscondition.text = "Digital files found on the Digital Scholarship Unit site are meant for research and private study used in compliance with copyright legislation. Access to digital images and text found on this website and the technical capacity to download or copy it does not imply permission to re-use. Prior written permission to publish, or otherwise use images and text found on the website must be obtained from the copyright holder. Please contact UTSC Library, Archives & Special Collections for further information."


    tree = ET.ElementTree(mods)
    tree.write(dest,encoding='utf-8',xml_declaration=True)


if __name__ == "__main__":

#    row = ['a','b']
#    defs = ['k1','k2']
#    dest = "."
    dest = "testarchive/MODS.xml"
    reader = csv.reader(codecs.open("006-1-4-5-1test.csv",encoding="utf-8")) # TODO TEXT ENCODING
    read_defs = False
    defs = []
    for row in reader:
        if not read_defs:
            defs = row
            read_defs = True
        else:
            csv_row_to_mods(row,defs,dest)
