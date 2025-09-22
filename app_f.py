import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Assuming these are your custom modules
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM


load_dotenv()


app = Flask(__name__)

@app.route('/blogs', methods=['POST'])
def create_blogs():
   
    data = request.get_json()

   
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    topic = data.get('topic', '')

    
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    graph_builder = GraphBuilder(llm)
    
    if topic:
        graph = graph_builder.setup_graph(usecase='topic')
        state = graph.invoke({'topic': topic})
        return jsonify({'data': state})
    
   
    return jsonify({'data': 'No topic provided'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)