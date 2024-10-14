new: workflow_dispatch.folder,
 run_on: .mhtml,
  add: wallet @etenterprises1.btc,
   amount: value,
    of: BITCOIN(.BTC)
using: .pyth,
 for: style,

add: deposit, 
 from: block, 
  on: Bitcoin.Net,
   block_info: `
  "block_hash": "00000000000000000001e529aa1b6b7433794e9b33723be85daeab7fdaabf1c0",
  "block_height": 832608,
  "block_index": 0,
  "hash": "2ea7f6a0d26b2b97dc2cc2a053d9e429fac2291b27318558ba3aa03791a37c31",
  "hex": "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff5e0360b40c1b2f5669614254432f4d696e656420627920727564656e69636b312f2cfabe6d6d822bf0878cd08c57e5b3d5a78280fa10fea8c1cf09a3a317aabd527dc2824569100000000000000010b4c5290aaa511d18fe3d13053d000000ffffffff03ef32cc26000000001976a914536ffa992491508dca0354e52f32a3a7a679a53a88ac00000000000000002b6a2952534b424c4f434b3a6de8b65efa82c97fe39adf6c3c722fa2eb1c20f57c5bf60988c32026005d7d0d0000000000000000266a24aa21a9ed2d7e92479b95b3bbbe453e13efa59a9744a8f2e194bf9c0b947abbdb439740050120000000000000000000000000000000000000000000000000000000000000000000000000",
  "addresses": [
    "18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX"
  ],
  "total": 650916591,
  "fees": 0,
  "size": 314,
  "vsize": 287,
  "preference": "low",
  "confirmed": "2024-03-01T00:46:00.501Z",
  "received": "2024-03-01T00:46:00.501Z",
  "ver": 1,
  "double_spend": false,
  "vin_sz": 1,
  "vout_sz": 3,
  "data_protocol": "unknown",
  "confirmations": 12962,
  "confidence": 1,
  "inputs": [
    {
      "output_index": -1,
      "script": "0360b40c1b2f5669614254432f4d696e656420627920727564656e69636b312f2cfabe6d6d822bf0878cd08c57e5b3d5a78280fa10fea8c1cf09a3a317aabd527dc2824569100000000000000010b4c5290aaa511d18fe3d13053d000000",
      "sequence": 4294967295,
      "script_type": "empty",
      "age": 832608
    }
  ],
  "outputs": [
    {
      "value": 650916591,
      "script": "76a914536ffa992491508dca0354e52f32a3a7a679a53a88ac",
      "spent_by": "7dd38d0a4b745e5e2b951a19537294d86b8c962e94338fed3dcc51219da93fbc",
      "addresses": [
        "18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX"
      ],
      "script_type": "pay-to-pubkey-hash"
    },
    {
      "value": 0,
      "script": "6a2952534b424c4f434b3a6de8b65efa82c97fe39adf6c3c722fa2eb1c20f57c5bf60988c32026005d7d0d",
      "addresses": null,
      "script_type": "null-data",
      "data_hex": "52534b424c4f434b3a6de8b65efa82c97fe39adf6c3c722fa2eb1c20f57c5bf60988c32026005d7d0d"
    },
    {
      "value": 0,
      "script": "6a24aa21a9ed2d7e92479b95b3bbbe453e13efa59a9744a8f2e194bf9c0b947abbdb43974005",
      "addresses": null,
      "script_type": "null-data",
      "data_hex": "aa21a9ed2d7e92479b95b3bbbe453e13efa59a9744a8f2e194bf9c0b947abbdb43974005"
    }
  ]
}`,
-get new -output addresses: with value, 