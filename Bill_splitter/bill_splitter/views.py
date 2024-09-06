import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple_bill_splitter(request):
    if request.method== "POST":
        data = json.loads(request.body)
        use_r = data.get('user_ids')
        t_bill=data.get('total_bill')
        length=len(use_r)
        return JsonResponse({"Share_per_person":t_bill/length})
    else:
        return JsonResponse({'error':'only POST method is allowed'})

# input must follow given pattern    
# {
#   "user_ids": [111, 112, 113, 114,],
#   "total_bill": 200.00
# }
    
@csrf_exempt
def uneven_bill_splitter(request):
    if request.method== "POST":
        data = json.loads(request.body)
        contibution = data.get('contributions')
        persons=len(contibution)
        t_bill=data.get('total_bill')
        even_share=t_bill/persons  
        lst=[] 
        credit=0
        debit=0
        
        for peoples in contibution:
            peo=peoples.get("user_id")
            cont=peoples.get("contribution")
            
            if cont < even_share:
                credit=abs(int(cont-even_share))
            else:  
                debit=abs(int(even_share-cont))
                
            result={
                "User_id":peo,
                "contibution":cont,
                "To_pay":debit,
                "To_receive":credit
            }    
            lst.append(result)
                  
        return JsonResponse({"Share_per_person":lst})
    else:
        return JsonResponse({'error':'only POST method is allowed'})
    
# input must follow given pattern   
# {
#   "contributions": [
#     {"user_id": 111, "contribution": 50},
#     {"user_id": 112, "contribution": 70},
#     {"user_id": 113, "contribution": 30},
#     {"user_id": 114, "contribution": 50}
#   ],
#   "total_bill": 200.00
# }
    
@csrf_exempt
def tax_tip_bill_splitter(request):
    if request.method== "POST":
        data = json.loads(request.body)
        use_r = data.get('user_ids')
        t_bill=data.get('total_bill')
        tax_percent=data.get('tax_percentage')
        tip_percent=data.get('tip_percentage')
        tax=t_bill*(tax_percent/100)
        tip=t_bill*(tip_percent/100)
        length=len(use_r)
        return JsonResponse({"Share_per_person":(t_bill+tax+tip)/length})
    else:
        return JsonResponse({'error':'only POST method is allowed'})
    
# input must follow given pattern    
# {
#   "user_ids": [111, 112, 113, 114,]
#   "total_bill": 200.00,
#   "tip_percentage": 10.0,   
#   "tax_percentage": 8.0     
# }    

@csrf_exempt
def discount_bill_splitter(request):
    if request.method== "POST":
        data = json.loads(request.body)
        use_r = data.get('user_ids')
        t_bill=data.get('total_bill')
        discount_percent=data.get('discount_percentage')
        discount=t_bill*(discount_percent/100)
        length=len(use_r)
        return JsonResponse({"Share_per_person":(t_bill-discount)/length})
    else:
        return JsonResponse({'error':'only POST method is allowed'})
    
# input must follow given pattern    
# {
#   "user_ids": [111, 112, 113, 114,],
#   "total_bill": 200,
#   "discount_percentage": 10 
# }
    
@csrf_exempt
def shared_item_splitter(request):
    if request.method== "POST":
        data = json.loads(request.body)
        user_ids = data.get('user_ids')
        dic={}
        
        for user in user_ids:
            dic[user]=0
            
        items=data.get('items')
        for item in items:
            item_price=item.get('item_price')
            item_share=item.get('share_with')
            per_person_share=item_price/len(item_share)
            
            for user in item_share:
                if user in dic:
                    dic[user] += per_person_share
        result=[]            
        for user,amount in dic.items():
            result.append({"User_id":user,"To pay":round(amount,2)})
        
        return JsonResponse({"Amount_due_of_each_user":result})
    else:
        return JsonResponse({'error':'only POST method is allowed'})    
    
# input must follow given pattern
#   {
#   "user_ids": [111, 112, 113, 114,],
#   "items": [
#     {"item_name": "Pizza", "item_price": 40.00, "share_with": [101, 102, 103]},
#     {"item_name": "Soda", "item_price": 10.00, "share_with": [102, 104]},
#     {"item_name": "Burger", "item_price": 20.00, "share_with": [103, 104]}
#   ]
# }
    