import jmespath
# jmespath is a query language for JSON.

j= {"people":[
    {
        "name":"Roshan",
        "age":34

    }
]}

print(jmespath.search("people[*].name",j))
