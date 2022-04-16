import string
import random


def generate_random_date():
    year = random.randint(1960, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    if month < 10:
        month = f'0{month}'
    if day < 10:
        day = f'0{day}'
    return f"{year}-{month}-{day}"


def generate_random_name(length):
    return (''.join(random.choice(string.ascii_lowercase) for i in range(length)))


def generate_unique_xml(issue_date, sender_name):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cec="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2">
    <cbc:UBLVersionID>2.1</cbc:UBLVersionID>
    <cbc:CustomizationID>urn:cen.eu:en16931:2017#conformant#urn:fdc:peppol.eu:2017:poacc:billing:international:aunz:3.0</cbc:CustomizationID>
    <cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>
    <cbc:ID>EBWASP1002</cbc:ID>
    <cbc:IssueDate>{issue_date}</cbc:IssueDate>
    <cbc:InvoiceTypeCode listAgencyID="6" listID="UNCL1001">380</cbc:InvoiceTypeCode>
    <cbc:DocumentCurrencyCode listAgencyID="6" listID="ISO4217">AUD</cbc:DocumentCurrencyCode>
    <cbc:BuyerReference>EBWASP1002</cbc:BuyerReference>
    <cac:AdditionalDocumentReference>
        <cbc:ID>ebwasp1002</cbc:ID>
    </cac:AdditionalDocumentReference>
    <cac:AccountingSupplierParty>
        <cac:Party>
            <cac:PartyIdentification>
                <cbc:ID schemeAgencyID="ZZZ" schemeID="0151">80647710156</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
                <cbc:Name>{sender_name}</cbc:Name>
            </cac:PartyName>
            <cac:PostalAddress>
                <cbc:StreetName>100 Business St</cbc:StreetName>
                <cbc:CityName>Dulwich Hill</cbc:CityName>
                <cbc:PostalZone>2203</cbc:PostalZone>
                <cac:Country>
                <cbc:IdentificationCode listAgencyID="6" listID="ISO3166-1:Alpha2">AU</cbc:IdentificationCode>
                </cac:Country>
            </cac:PostalAddress>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>{sender_name}</cbc:RegistrationName>
                <cbc:CompanyID schemeAgencyID="ZZZ" schemeID="0151">80647710156</cbc:CompanyID>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:AccountingCustomerParty>
        <cac:Party>
            <cac:PartyName>
                <cbc:Name>Awolako Enterprises Pty Ltd</cbc:Name>
            </cac:PartyName>
            <cac:PostalAddress>
                <cbc:StreetName>Suite 123 Level 45</cbc:StreetName>
                <cbc:AdditionalStreetName>999 The Crescent</cbc:AdditionalStreetName>
                <cbc:CityName>Homebush West</cbc:CityName>
                <cbc:PostalZone>2140</cbc:PostalZone>
                <cac:Country>
                <cbc:IdentificationCode listAgencyID="6" listID="ISO3166-1:Alpha2">AU</cbc:IdentificationCode>
                </cac:Country>
            </cac:PostalAddress>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>Awolako Enterprises Pty Ltd</cbc:RegistrationName>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingCustomerParty>
    <cac:PaymentMeans>
        <cbc:PaymentMeansCode listAgencyID="6" listID="UNCL4461">1</cbc:PaymentMeansCode>
        <cbc:PaymentID>EBWASP1002</cbc:PaymentID>
    </cac:PaymentMeans>
    <cac:PaymentTerms>
        <cbc:Note>As agreed</cbc:Note>
    </cac:PaymentTerms>
    <cac:TaxTotal>
        <cbc:TaxAmount currencyID="AUD">10.00</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="AUD">100.00</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="AUD">10.00</cbc:TaxAmount>
            <cac:TaxCategory>
                <cbc:ID schemeAgencyID="6" schemeID="UNCL5305">S</cbc:ID>
                <cbc:Percent>10.0</cbc:Percent>
                <cac:TaxScheme>
                <cbc:ID schemeAgencyID="6" schemeID="UN/ECE 5153">GST</cbc:ID>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:TaxTotal>
    <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="AUD">100.00</cbc:LineExtensionAmount>
        <cbc:TaxExclusiveAmount currencyID="AUD">100.00</cbc:TaxExclusiveAmount>
        <cbc:TaxInclusiveAmount currencyID="AUD">110.00</cbc:TaxInclusiveAmount>
        <cbc:PayableRoundingAmount currencyID="AUD">0.00</cbc:PayableRoundingAmount>
        <cbc:PayableAmount currencyID="AUD">110.00</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    <cac:InvoiceLine>
        <cbc:ID>1</cbc:ID>
        <cbc:InvoicedQuantity unitCode="C62" unitCodeListID="UNECERec20">500.0</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="AUD">100.00</cbc:LineExtensionAmount>
        <cac:Item>
            <cbc:Name>pencils</cbc:Name>
            <cac:ClassifiedTaxCategory>
                <cbc:ID schemeAgencyID="6" schemeID="UNCL5305">S</cbc:ID>
                <cbc:Percent>10.0</cbc:Percent>
                <cac:TaxScheme>
                <cbc:ID schemeAgencyID="6" schemeID="UN/ECE 5153">GST</cbc:ID>
                </cac:TaxScheme>
            </cac:ClassifiedTaxCategory>
        </cac:Item>
        <cac:Price>
            <cbc:PriceAmount currencyID="AUD">0.20</cbc:PriceAmount>
            <cbc:BaseQuantity unitCode="C62" unitCodeListID="UNECERec20">1.0</cbc:BaseQuantity>
        </cac:Price>
    </cac:InvoiceLine>
    </Invoice>"""
