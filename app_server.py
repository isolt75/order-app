from flask import Flask,render_template,request

app = Flask(__name__)

# 중분류 Coffee, Tea, Smoothie, Dessert

MIDDLE_SEQ = [
    {
        "id": 1,
        "name":"Coffee"
    },
    {
        "id": 2,
        "name":"Tea"
    },
    {
        "id": 3,
        "name":"Smoothie"},
    {
        "id": 4,
        "name":"Dessert"}
]
SELECT_MIDDLE_SEQ = None
SELECT_MIDDLE_SEQ2 = None
SELECT_MIDDLE_SEQ3 = None

MENUS = [

    {
        "id" : 1,
        "name" : "아메리카노",
        "price" : 3000,
        "parntId" : 1
    },
    {
        "id" : 2,
        "name" : "카페라떼",
        "price" : 4000,
        "parntId" : 1
    },
    {
        "id" : 3,
        "name" : "요거트스무디",
        "price" : 4500,
        "parntId" : 3
    },
    {
        "id" : 4,
        "name" : "딸기스무디",
        "price" : 4500,
        "parntId" : 3
    },
    {
        "id" : 5,
        "name" : "캐모마일",
        "price" : 4000,
        "parntId" : 2
    },
    {
        "id" : 6,
        "name" : "유자차",
        "price" : 4000,
        "parntId" : 2
    },
    {
        "id" : 7,
        "name" : "티라미수",
        "price" : 5500,
        "parntId" : 4
    },
    {
        "id" : 8,
        "name" : "우유케익",
        "price" : 4500,
        "parntId" : 4
    },
]
# 매장 포장 선택 화면 진입

@app.route("/")
def goIndex() :
    return render_template("index.html")

@app.route("/step1")
def goStep1() :
    return render_template("step1.html", datum=MIDDLE_SEQ)

@app.route("/step2")
def goStep2() :
    return render_template("step2.html")

@app.route("/step3")
def goStep3() :
    return render_template("step3.html")       

@app.route("/order")
def goOrder() :
    return render_template("order.html")    

@app.route("/pay1")
def goPay1() :
    return render_template("pay1.html")

@app.route("/membership")
def goMembership() :
    return render_template("membership.html") 

@app.route("/phone")
def goPhone() :
    return render_template("phone.html") 

@app.route("/userCheck")
def goUserCheck() :
    return render_template("userCheck.html")   

@app.route("/pay2")
def goPay2() :
    return render_template("pay2.html")   
 
@app.route("/complete")
def goComplete() :
    return render_template("complete.html") 

@app.route("/final")
def goFinal() :
    return render_template("final.html") 
  
@app.route("/step1_select")
def selectStep1():
    param = request.args.get("middleData")
    SELECT_MIDDLE_SEQ = param
    

    arr =[]
    for item in MENUS : 
        if(int(item["parntId"]) == int(param)):
            arr.append(item)

    return render_template("step2.html",list=arr)
@app.route("/step2_select")
def selectStep2():
    param = request.args.get("middleData")
    global SELECT_MIDDLE_SEQ2
    SELECT_MIDDLE_SEQ2 = param
    

    return render_template("step3.html",list=SELECT_MIDDLE_SEQ2)

@app.route("/step3_select")
def selectStep3():
    param = request.args.get("option")


    SELECT_MIDDLE_SEQ3 = param
    
    return render_template("order.html",option=SELECT_MIDDLE_SEQ3,menu=SELECT_MIDDLE_SEQ2)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)