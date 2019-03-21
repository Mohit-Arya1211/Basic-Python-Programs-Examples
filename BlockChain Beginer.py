import hashlib
import json

block_code = {
    'prev_hash': None,
    'transactions': [1, 3, 4, 2]
}

block_code_serialized = json.dumps(block_code, sort_keys=True).encode('utf-8')
block_code_hash = hashlib.sha256(block_code_serialized).hexdigest()
block_2 = {
    'prev_hash': block_code_hash,
    'transaction': [3, 3, 3, 88, 70, 400]
}
block_2_serialized = json.dumps(block_2, sort_keys=True).encode('utf-8')
block_2_hash = hashlib.sha256(block_2_serialized).hexdigest()

block_3 = {
    'prev_hash': block_code_hash,
    'transaction': [3, 4, 4, 8, 7, 32]
}
block_3_serialized = json.dumps(block_3, sort_keys=True).encode('utf-8')
block_3_hash = hashlib.sha256(block_3_serialized).hexdigest()


def hash_blocks(blocks):
 prev_hash = None
 for block in blocks:
  block['prev_hash'] = prev_hash
  block_serialized = json.dumps(block, sort_keys=True).encode('utf-8')
  block_hash = hashlib.sha256(block_serialized).hexdigest()
  prev_hash = block_hash

 return prev_hash

print("Original hash")
print(hash_blocks([block_code, block_2, block_3]))

print("Tampering the data")
block_code['transactions'][0] = 3
