from uuid import uuid4
from flask import Flask, jsonify, request
from dlt import DLT

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the DLT
dlt = DLT()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Mine a new block.
    """
    last_block = dlt.last_block
    last_proof = last_block['proof']
    proof = dlt.proof_of_authority(last_proof)

    # Reward for finding the proof
    dlt.new_data({
        'users': '0',
        'data': [],
        'dh_parameters': '',
        'server_public_key': '',
        'receiver_public_key': '',
        'sender_public_key': '',
        'sender_zkp_status': 'Completed',
        'receiver_zkp_status': 'Completed',
        'sender_balance': 0,
        'receiver_balance': 0,
        'authentification': 'Completed',
        'Sufficient_amount': 'Completed',
        'sender_wallet_hash': '',
        'receiver_wallet_hash': ''
    })

    # Forge the new block by adding it to the chain
    block = dlt.new_block(proof)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'data': block['data'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Create a new transaction.
    """
    values = request.get_json()

    # Check that the required fields are in the POST data
    required = ['users', 'data', 'dh_parameters', 'server_public_key', 'receiver_public_key', 'sender_public_key']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction
    index = dlt.new_data(values)

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """
    Return the full blockchain.
    """
    response = {
        'chain': dlt.chain,
        'length': len(dlt.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """
    Register new nodes.
    """
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        dlt.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(dlt.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """
    Consensus algorithm to resolve
