from django.shortcuts import render, redirect

def index(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/index.html')

def bb(request):
   #return  redirect('/') #go to homepage
   return render(request, 'bbmodule/bblist.html')

def bb1(request, bID):
    b1 = {'id':101,'title':'make up artis','name':'sara ,Hifa'}
    b2 = {'id':102,'title':'Hair stylist','name':'noura'}
    b3 = {'id':103,'title':'Dresses','name':'Alanoud'}
    b4 = {'id':104,'title':'Wedding decoration','name':'shahad'}

    targetbb1 = None
    if b1['id'] == bID: targetbb1 = b1
    if b2['id'] == bID: targetbb1 = b2
    if b3['id'] == bID: targetbb1 = b3
    if b4['id'] == bID: targetbb1 = b4

    if targetbb1 == None: return redirect('/bb')


    context = {'bb1':targetbb1}
    return render(request, 'bbmodule/bb1.html', context)

