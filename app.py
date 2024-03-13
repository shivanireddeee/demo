from flask import Flask, render_template, request, redirect, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Supabase client
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/supabase_data')
def supabase_data():
    # Fetch data from the 'test' table
    response = supabase.table('test').select('*').execute()
    # Use the 'data' attribute to access the data returned by the query
    data = response['data']
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    id = data['id']
    name = data['name']
    # Insert data into 'test' table
    response = supabase.table('test').insert({'id': id, 'name': name}).execute()
    return '', 204

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    # Delete record from 'test' table
    response = supabase.table('test').delete().eq('id', id).execute()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
