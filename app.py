from flask import Flask, render_template, request, redirect
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
    # Fetch data from the 'test' table
    response = supabase.table('test').select('*').execute()
    # Use the 'data' attribute to access the data returned by the query
    data = response.data
    return render_template('index.html', data=data)



@app.route('/submit', methods=['POST'])
def submit_form():
    id = request.form['id']
    name = request.form['name']
    # Insert data into 'test' table
    response = supabase.table('test').insert({'id': id, 'name': name}).execute()
    return redirect('/')


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    # Delete record from 'test' table
    response = supabase.table('test').delete().eq('id', id).execute()
    return redirect('/')

# @app.route('/update/<int:id>', methods=['UPDATE'])
# def update_record(id):
#     response = supabase.table('test').update({'id': 'id'}).eq('id', id).execute()
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)














# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



