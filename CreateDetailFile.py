import csv

def detail_file(soup, filename, count):
    # this section will be for single tags
    issuer_cik = soup.find('issuerCik').get_text()
    issuer_name = soup.find('issuerName').get_text()
    issuer_symbol = soup.find('issuerTradingSymbol').get_text()
    form_type = soup.find('transactionFormType').get_text()
    # officer_title = soup.find('officerTitle').get_text()

    try:


        # this section will be for tags that have the "Value" tag with the results
        # need to 're-soup' to isolate the single value tag

        if not soup.transactionAmounts.transactionAcquiredDisposedCode.value:
            disposal_code = 'NA'
        else:
            disposal_code = soup.transactionAmounts.transactionAcquiredDisposedCode.value.get_text()

        if not soup.transactionAmounts.transactionShares.value:
            shares = 'NA'
        else:
            shares = soup.transactionAmounts.transactionShares.value.get_text()

        if not soup.transactionAmounts.transactionPricePerShare.value:
            price_per_share = 'NA'
        else:
            price_per_share = soup.transactionAmounts.transactionPricePerShare.value.get_text()

        if not soup.ownershipNature.directOrIndirectOwnership.value:
            direct_or_indirect_ownership = 'NA'
        else:
            direct_or_indirect_ownership = soup.ownershipNature.directOrIndirectOwnership.value.get_text()

        if not soup.transactionDate.value:
            transaction_date = 'NA'
        else:
            transaction_date = soup.transactionDate.value.get_text()

        if not soup.securityTitle.value:
            security_title = 'NA'
        else:
            security_title = soup.securityTitle.value.get_text()

        if not soup.postTransactionAmounts.sharesOwnedFollowingTransaction.value:
            sharesOwnedFollowingTransaction = 'NA'
        else:
            sharesOwnedFollowingTransaction = soup.postTransactionAmounts.sharesOwnedFollowingTransaction.value.get_text()

    except Exception as e:
        print("type error: " + str(e) + ": " + filename)

    # by using with statement close() file is not necessary
    try:

        with open('c:\\temp\\form4.csv', 'a', newline='') as csvfile:

            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if count == 0:
                writer.writerow(["transaction_date", "issuer_cik", "issuer_name", "issuer_symbol",
                                 "form_type", "disposal_code", "shares", "price_per_share",
                                 "direct_or_indirect_ownership",
                                 "security_title", "sharesOwnedFollowingTransaction", "Filename"])

            writer.writerow([transaction_date, issuer_cik, issuer_name, issuer_symbol,
                             form_type,disposal_code, shares, price_per_share, direct_or_indirect_ownership,
                             security_title, sharesOwnedFollowingTransaction, filename])
    except Exception as e:
        print("type error: " + str(e) + ": " + filename)
