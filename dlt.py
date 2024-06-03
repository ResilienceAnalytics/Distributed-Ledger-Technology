import hashlib
import json
from time import time
import requests

class DLT:
    """
    A simple Distributed Ledger Technology implementation to record session data.

    Attributes:
        chain (list): A list to store the chain of blocks.
        current_data (list): A list to store the current session data to be added to the next block.
        nodes (set): A set to store the network nodes.
    """
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def register_node(self, address):
        """
        Add a new node to the list of nodes.

        Args:
            address (str): Address of the node. Eg. 'http://192.168.0.5:5000'
        """
        parsed_url = address
        self.nodes.add(parsed_url)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the DLT.

        Args:
            proof (int): The proof given by the Proof of Authority algorithm.
            previous_hash (str, optional): Hash of the previous block. Defaults to None.

        Returns:
            dict: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, session_data):
        """
        Add new session data to the list of data.

        Args:
            session_data (dict): The session data to be added.

        Returns:
            int: The index of the block that will hold this data.
        """
        self.current_data.append({
            'users': session_data['users'],
            'data': session_data.get('data', []),
            'dh_parameters': session_data['dh_parameters'],
            'server_public_key': session_data['server_public_key'],
            'receiver_public_key': session_data['receiver_public_key'],
            'sender_public_key': session_data['sender_public_key'],
            'sender_zkp_status': session_data.get('sender_zkp_status', 'Pending'),
            'receiver_zkp_status': session_data.get('receiver_zkp_status', 'Pending'),
            'sender_balance': session_data.get('sender_balance', 0),
            'receiver_balance': session_data.get('receiver_balance', 0),
            'authentification': session_data.get('authentification', 'Pending'),
            'Sufficient_amount': session_data.get('Sufficient_amount', 'Pending'),
            'sender_wallet_hash': session_data.get('sender_wallet_hash', ''),
            'receiver_wallet_hash': session_data.get('receiver_wallet_hash', '')
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.

        Args:
            block (dict): Block.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Get the last block in the chain.

        Returns:
            dict: The last block in the chain.
        """
        return self.chain[-1]

    def proof_of_authority(self, last_proof):
        """
        Simulate a Proof of Authority mechanism (for demonstration purposes).

        Args:
            last_proof (int): The proof of the previous block.

        Returns:
            int: The new proof.
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the proof (for demonstration purposes, a simple condition).

        Args:
            last_proof (int): The proof of the previous block.
            proof (int): The current proof.

        Returns:
            bool: True if the proof is valid, False otherwise.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def resolve_conflicts(self):
        """
        Consensus Algorithm, resolves conflicts by replacing our chain with the longest one in the network.

        Returns:
            bool: True if our chain was replaced, False if not.
        """
        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid.

        Args:
            chain (list): A blockchain.

        Returns:
            bool: True if valid, False otherwise.
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True
