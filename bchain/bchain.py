"""
Blockchain Main Functions

Creates the block and hashes.
"""
import os
import logging
from urllib.parse import parse_qsl
from hashlib import sha256
from bchain.pow import proof_of_work
logger = logging.getLogger(__name__)
fh = logging.FileHandler(f'{__name__}.log')
logger.addHandler(fh)
logger.setLevel(logging.INFO)


DATA_HEADER = "Date|Time|EventID|Appl.ID |ActivePWR |ReactivePwr|Voltage|Intensity |HASH"
DATA_RECORDS = ["10Mar2015 0:00:00 1201210 9b75a5178a 2.58 0.136 241.97 10.6",
                "10Mar2015 0:01:00 1201211 9b75a5178f 2.552 0.1 241.75 10.4",
                "10Mar2015 0:02:00 1201212 9b75a51791 2.55 0.1 241.64 10.4",
                "10Mar2015 0:03:00 1201213 9b75a5178d 2.55 0.1 241.71 10.4",
                "10Mar2015 0:04:00 1201214 9b75a5178b 2.554 0.1 241.98 10.4",
                "10Mar2015 0:05:00 1201215 9b75a5178f 2.55 0.1 241.83 10.4",
                "10Mar2015 0:06:00 1201216 9b75a51790 2.534 0.09 241.07 10.4",
                "10Mar2015 0:07:00 1201217 9b75a51791 2.484 0.21 241.29 10.2",
                "10Mar2015 0:08:00 1201218 9b75a5178a 2.468 0.32 241.23 10.2",
                "10Mar2015 0:09:00 1201219 9b75a51793 2.48 0.54 242.28 10.2",
                ]
LINE_BREAK = ""
NONCE = '23df'
FIRST_HASH = ("0000100308e7e0bea95a3e88e4e406c3"
              "7133f0929c80866bda04bc0bce53a15")
TITLE = 'Blockchain1'
INITIAL_BLOCK_NO = 432


def create_block():
    """Creates the pre-defined block"""
    data = [DATA_HEADER]
    records = [f">>> {rec}" for rec in DATA_RECORDS]
    return LINE_BREAK.join(data + records)


def create_hash(request):
    """Creates the hash based on parameters `previous_hash`
    and `eventData` in the request object.
    """
    encoder = sha256()
    params = dict(parse_qsl(request.query_string))
    logger.info("Hash values: %s, %s", *params.values())
    return proof_of_work(params.get(b'previous_hash'),
                         params.get(b'eventData'))


def create_block_chain(previous_hash, nonce, prefix="0000"):
    """Creates 6 (+ 1, the first) blocks in the chain, using `previous_hash`
    and `nonce` as the starting element.
    """
    hash_list = [(nonce, previous_hash)]
    block = create_block()
    for i in range(1, 7):
        nonce, hash_code = proof_of_work(hash_list[i - 1][1].encode(),
                                         block.encode(),
                                         prefix=prefix)
        hash_list.append((nonce, hash_code))

    return hash_list


def create_data(number_of_hash_codes):
    """Generate the data for the espeficied number of hash codes,
    plus the previous code.
    """
    nonces, hash_codes = zip(*create_block_chain(FIRST_HASH, NONCE))
    params = {'title': TITLE,
              'block_no': [INITIAL_BLOCK_NO + count for count in range(number_of_hash_codes)],
              'event_data': [create_block()] * number_of_hash_codes,
              'nonce_list': nonces[1:number_of_hash_codes + 1],
              'hash_list': hash_codes[1:number_of_hash_codes + 1],
              'previous_hash': hash_codes[:number_of_hash_codes],
              'production': os.environ.get('PRODUCTION', False),
              'size': number_of_hash_codes,
              }
    return params
