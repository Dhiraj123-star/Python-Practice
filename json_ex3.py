# serialising is the process of encoding JSON.
import json
var ={
    "Subjects":{
        "Maths":90,
        "Science":99,
        "Computer Science":100
    }
}
with open("Sample.json","w") as f:
    json.dump(var,f)

print("object dumped successfully!!")