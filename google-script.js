// This script should be imported into google scripts
function importPrices() {
  var sheet = SpreadsheetApp.getActiveSheet()

  var ipfsHash = Browser.inputBox(
    'Enter IPFS hash',
    'Paste the IPFS hash here:',
    Browser.Buttons.OK_CANCEL
  )
  if (ipfsHash === 'cancel' || ipfsHash === '') {
    return
  }

  var jsonUrl = 'https://gateway.pinata.cloud/ipfs/' + ipfsHash

  sheet.getRange(1, 1).setValue('Coin')
  sheet.getRange(1, 2).setValue('Price')

  var response = UrlFetchApp.fetch(jsonUrl)
  var json = JSON.parse(response.getContentText())

  var i = 0
  for (var coin in json) {
    var price = json[coin]

    sheet.getRange(i + 2, 1).setValue(coin)
    sheet.getRange(i + 2, 2).setValue(price)
    i++
  }
}
