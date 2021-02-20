from flask import Flask, request, abort, jsonify
import pickle
app=Flask(__name__)

@app.route("/student_performance_prediction")
def home():
    model = pickle.load(open('model.pkl', 'rb'))
    data = request.get_json()
    return jsonify({
                'success': True,
                'data': model.predit([
                            data["gender"],
                            data["Nationalty"],
                            data["place_of_birth"],
                            data["stage"],
                            data["grade"],
                            data["section"],
                            data["topic"],
                            data["semester"],
                            data["relation"],
                            data["raisedhands"],
                            data["visted_resource"],
                            data["AnnouncementsView"],
                            data["Discussion"],
                            data["ParentAnsweringSurvey"],
                            data["ParentschoolSatisfaction"],
                            data["StudentAbsenceDays"],
                        ]),
            })


@app.route('/', methods=['GET'])
    def hi():
        return jsonify({
            'hello': hi
        })

if __name__ == "__main__":
    app.run()(debug=False,host='0.0.0.0')
