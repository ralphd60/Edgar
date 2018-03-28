import csv

def detail_file(soup, filename, count):
    # this section will be for single tags
    issuer_cik = soup.find('issuerCik').get_text()
    issuer_name = soup.find('issuerName').get_text()
    issuer_symbol = soup.find('issuerTradingSymbol').get_text()
    form_type = soup.find('documentType').get_text()
    # isDirector = soup.find('isDirector').get_text()
    # isOfficer = soup.find('isOfficer').get_text()
    footnotes = soup.find_all('footnote')
    is_director = "NA"
    is_officer = "NA"
    nonderivative_tags = soup.find_all('nonDerivativeTransaction')
    for tags in nonderivative_tags:

        try:
            # this section will be for tags that have the "Value" tag with the results
            # need to 're-soup' to isolate the single value tag

            if not tags.transactionAmounts.transactionAcquiredDisposedCode.value:
                disposal_code = 'NA'
            else:
                disposal_code = tags.transactionAmounts.transactionAcquiredDisposedCode.value.get_text()

            if not tags.transactionAmounts.transactionShares.value:
                shares = 'NA'
            else:
                shares = tags.transactionAmounts.transactionShares.value.get_text()

            if not tags.transactionAmounts.transactionPricePerShare.value:
                price_per_share = 'NA'
            else:
                price_per_share = tags.transactionAmounts.transactionPricePerShare.value.get_text()

            if not tags.ownershipNature.directOrIndirectOwnership.value:
                direct_or_indirect_ownership = 'NA'
            else:
                direct_or_indirect_ownership = tags.ownershipNature.directOrIndirectOwnership.value.get_text()

            if not tags.transactionDate.value:
                transaction_date = 'NA'
            else:
                transaction_date = tags.transactionDate.value.get_text()

            if not tags.securityTitle.value:
                security_title = 'NA'
            else:
                security_title = tags.securityTitle.value.get_text()

            if not tags.postTransactionAmounts.sharesOwnedFollowingTransaction.value:
                shares_owned_following_transaction = 'NA'
            else:
                shares_owned_following_transaction = \
                    tags.postTransactionAmounts.sharesOwnedFollowingTransaction.value.get_text()

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
                                     "security_title", "sharesOwnedFollowingTransaction", "Director",
                                     "Officer", "Footnotes", "Filename"])
                    count = count + 1
                writer.writerow([transaction_date, issuer_cik, issuer_name, issuer_symbol,
                                 form_type,disposal_code, shares, price_per_share, direct_or_indirect_ownership,
                                 security_title, shares_owned_following_transaction,is_director,
                                 is_officer, footnotes, filename])
        except Exception as e:
            print("type error: " + str(e) + ": " + filename)

    return count