import csv
from bs4 import BeautifulSoup

def detail_file(soup, filename):

    # this section will be for single tags
    issuer_cik = soup.find('issuerCik').get_text()
    issuer_name = soup.find('issuerName').get_text()
    issuer_symbol = soup.find('issuerTradingSymbol').get_text()
    form_type = soup.find('transactionFormType').get_text()
    officer_title = soup.find('officerTitle').get_text()


    # this section will be for tags that have the "Value" tag with the results
    # need to 're-soup' to isolate the single value tag
    try:
        disposal_code_soup = soup.find('transactionAcquiredDisposedCode')
        disposal_code = disposal_code_soup.find('value').get_text()
        shares_soup = soup.find('transactionShares')
        shares = shares_soup.find('value').get_text()
        price_per_share_soup = soup.find('transactionPricePerShare')
        price_per_share = price_per_share_soup.find('value').get_text()
        direct_or_indirect_ownership_soup = soup.find('directOrIndirectOwnership')
        direct_or_indirect_ownership = direct_or_indirect_ownership_soup.find('value').get_text()
        transaction_date_soup = soup.find('transactionDate')
        transaction_date = transaction_date_soup.find('value').get_text()
        security_title_soup = soup.find('securityTitle')
        security_title = security_title_soup.find('value').get_text()
    except Exception as e:
        print("type error: " + str(e) + ": " + filename)

    # by using with statement close() file is not necessary
    try:
        with open('c:\\temp\\form4.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([transaction_date, issuer_cik, issuer_name, issuer_symbol, form_type,disposal_code, shares, price_per_share, direct_or_indirect_ownership, officer_title, security_title])
    except Exception as e:
        print("type error: " + str(e) + ": " + filename)

    # using csv module (see import)
    # file = open('c:\\temp\\form4.csv',mode='a',)
    # file.write (issuer_cik, issuer_name, issuer_symbol, form_type, officer_title )
    # file.close()

    # try:
    #     print("CIK code: " + issuer_cik)
    # except Exception as e:
    #     print("type error: " + str(e))
    # try:
    #     print("Disposable code (A- bought, D - sold): " + disposal_code_soup.find('value').get_text())
    # except Exception as e:
    #     print("type error: " + str(e))
    # try:
    #     print("Number of shares in transaction: " + shares_soup.find('value').get_text())
    # except Exception as e:
    #     print("type error: " + str(e))
    # try:
    #     print("Price per share: " + price_per_share_soup.find('value').get_text())
    # except Exception as e:
    #     print("type error: " + str(e))
    # try:
    #     print ("Direct or Indirect Ownership: " + direct_or_indirect_ownership_soup.find('value').get_text())
    # except Exception as e:
    #     print("type error: " + str(e))
    # try:
    #     print("Transaction date: " + transaction_date_soup.find('value').get_text())
    # except Exception as e:
    #     print("type error: " + str(e))