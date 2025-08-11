@app.route('/test_gas', methods=['POST'])
def test_gas():
    """Test-only endpoint for prepaid gas"""
    try:
        # Hardcoded test hash
        test_hash = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
        
        # Your existing prepaid gas function
        tx_id = vechain_prepaid_gas_flow(test_hash)
        
        return jsonify({
            "status": "success",
            "tx_id": tx_id,
            "explorer_link": f"https://explore-testnet.vechain.org/transactions/{tx_id}"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
