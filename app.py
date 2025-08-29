from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USER_INFO = {
    "user_id": "lazim_afraz",  # your_name_ddmmyyyy (lowercase)
    "email": "lazim0418@gmail.com",         # your email
    "roll_number": "22BCT0265"        
}

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        input_array = data['data']
        
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        all_letters = []
        number_sum = 0
        
        # Process each item
        for item in input_array:
            try:
                # Try to convert to number
                num = int(item)
                number_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            except:
                # Not a number, check each character
                for char in item:
                    if char.isalpha():
                        alphabets.append(char.upper())
                        all_letters.append(char)
                    elif not char.isalnum():
                        special_characters.append(char)
        
        # Remove duplicate alphabets
        alphabets = list(dict.fromkeys(alphabets))
        special_characters = list(dict.fromkeys(special_characters))
        
        # Create concat_string (reverse + alternating caps)
        concat_string = ""
        if all_letters:
            reversed_letters = all_letters[::-1]
            for i, letter in enumerate(reversed_letters):
                if i % 2 == 0:
                    concat_string += letter.lower()
                else:
                    concat_string += letter.upper()
        
        return jsonify({
            "is_success": True,
            "user_id": USER_INFO["user_id"],
            "email": USER_INFO["email"],
            "roll_number": USER_INFO["roll_number"],
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(number_sum),
            "concat_string": concat_string
        }), 200
        
    except:
        return jsonify({"is_success": False}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
