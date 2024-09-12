import requests
from web3 import Web3
import json
from tqdm import tqdm
import math
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
progress = ttk.Progressbar(root, mode="determinate")
def update_progressbar(value):
    progress["value"] = value
    progress.update()

uniswap_v2_abi = json.loads(
    '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

)

YOUR_ALCHEMY_KEY=""
alchemy = f"https://polygon-mainnet.g.alchemy.com/v2/{YOUR_ALCHEMY_KEY}"

w3 = Web3(Web3.HTTPProvider(alchemy))

assert w3.isConnected(), "Connection to Polygon network failed"

etherscan_api_key = "YOUR_ETHERSCAN_KEY"


def get_txn_list(address, startblock, endblock, sort, api_key, num_transactions):
    transactions = []
    page_size = 10000  # You can set this to a smaller value if you prefer smaller chunks

    num_pages = math.ceil(num_transactions / page_size)

    for page in range(num_pages):
        offset = page * page_size
        url = f"https://api.polygonscan.com/api?module=account&action=txlist&address={address}&startblock={startblock}&endblock={endblock}&sort={sort}&offset={offset}&apikey={api_key}"
        print(url)
        response = requests.get(url)
        data = response.json()

        if data["status"] == "1":
            transactions.extend(data["result"])
        else:
            raise Exception("Error fetching transaction list: " + data["message"])

        # Stop fetching if we already have enough transactions
        if len(transactions) >= num_transactions:
            break

    return transactions[:num_transactions]


def get_successful_arbitrage_transactions(contract_address, num_transactions):
    contract = w3.eth.contract(address=contract_address, abi=uniswap_v2_abi)
    txn_list = get_txn_list(contract_address, 0, "latest", "desc", etherscan_api_key,num_transactions)

    # Filter transactions with a positive net gain
    arbitrage_transactions = []
    c=0

    for txn in txn_list:
        input_token, output_token, input_amount, output_amount = parse_swap_data(txn)
        update_progressbar(100 * c / num_transactions)
        if input_token!=None and output_token!=None and input_amount!=None and output_amount!=None:
            if input_token == output_token and output_amount >= input_amount:
                arbitrage_transactions.append(txn)
        c=c+1
    print("finished scanning")
    return arbitrage_transactions



def parse_swap_data(txn):
    contract = w3.eth.contract(address=w3.toChecksumAddress(contract_address), abi=uniswap_v2_abi)
    # Function signatures for swap functions in Uniswap forks
    function_signatures = [
        "swapExactTokensForTokensSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)",
        "swapExactETHForTokensSupportingFeeOnTransferTokens(uint256,address[],address,uint256)",
        "swapExactTokensForETHSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)",
        "swapExactTokensForTokens(uint256,uint256,address[],address,uint256)",
        "swapTokensForExactTokens(uint256,uint256,address[],address,uint256)",
        "swapExactETHForTokens(uint256,address[],address,uint256)",
        "swapTokensForExactETH(uint256,uint256,address[],address,uint256)",
        "swapExactTokensForETH(uint256,uint256,address[],address,uint256)",
        "swapETHForExactTokens(uint256,address[],address,uint256)"
    ]

    input_token = None
    output_token = None
    input_amount = None
    output_amount = None

    for sig in function_signatures:
        method_id = w3.sha3(text=sig)[:10]

        if txn["input"][:10] == method_id.hex()[0:10]:
            # Decode transaction input data

            inputs=contract.decode_function_input(txn["input"])

            # Get token addresses and amounts depending on the swap function
            if "swapExactTokensForTokens" in sig or "swapExactTokensForETH" in sig:
                input_token = inputs[1]['path'][0]
                output_token = inputs[1]['path'][-1]
                input_amount = inputs[1]['amountIn']
                # output_amount is not available, use amountOutMin as an approximation
                output_amount = inputs[1]['amountOutMin']
            elif "swapExactETHForTokens" in sig:
                input_token = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
                output_token = inputs[1]['path'][-1]
                input_amount = int(txn["value"], 16)
                # output_amount is not available, use amountOutMin as an approximation
                output_amount = inputs[1]['amountOutMin']
            elif "swapTokensForExactTokens" in sig or "swapTokensForExactETH" in sig:
                input_token = inputs[1]['path'][0]
                output_token = inputs[1]['path'][-1]
                # input_amount is not available, use amountInMax as an approximation
                input_amount = inputs[1]['amountInMax']
                output_amount = inputs[1]['amountOut']
            elif "swapETHForExactTokens" in sig:
                input_token = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
                output_token = inputs[1]['path'][-1]
                input_amount = int(txn["value"], 16)
                output_amount = inputs[1]['amountOut']

            break

    return input_token, output_token, input_amount, output_amount

contract_address = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"
num_transactions = 1000



successful_arbitrages = []

def on_start():
    global contract_address
    global num_transactions
    contract_address = contract_address_entry.get()
    num_transactions = int(num_transactions_entry.get())
    network = networks_combobox.get()

    if network == "Polygon":
        global successful_arbitrages
        successful_arbitrages = get_successful_arbitrage_transactions(w3.toChecksumAddress(contract_address), num_transactions)
        results_listbox.delete(0, tk.END)

        for txn in successful_arbitrages:
            results_listbox.insert(tk.END, f"{txn['hash']}")


# GUI setup

root.title("Arbitrage Transactions Finder")

# Create and place widgets
contract_address_label = ttk.Label(root, text="Smart Contract Address:")
contract_address_entry = ttk.Entry(root)
num_transactions_label = ttk.Label(root, text="Number of Transactions:")
num_transactions_entry = ttk.Entry(root)

networks = ["Polygon"]
networks_var = tk.StringVar(root)
networks_var.set("Polygon")
networks_combobox = ttk.Combobox(root, values=networks, textvariable=networks_var, state="readonly")

start_button = ttk.Button(root, text="Start", command=on_start)

results_listbox = tk.Listbox(root)

contract_address_label.grid(row=0, column=0, sticky="w")
contract_address_entry.grid(row=0, column=1, sticky="ew")
num_transactions_label.grid(row=1, column=0, sticky="w")
num_transactions_entry.grid(row=1, column=1, sticky="ew")

networks_combobox.grid(row=2, column=0, columnspan=2, sticky="ew")
start_button.grid(row=3, column=0)
progress.grid(row=4, column=0, columnspan=2, sticky="ew")
results_listbox.grid(row=5, column=0, columnspan=2, sticky="nsew")

root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)

def save_results():

    global successful_arbitrages
    with open("successful_arbitrages.txt", "w") as f:
        for txn in successful_arbitrages:
            f.write(f"{txn['hash']}\n")

# Add Save button
save_button = ttk.Button(root, text="Save", command=save_results)
save_button.grid(row=3, column=1)



# Run the GUI event loop
root.mainloop()