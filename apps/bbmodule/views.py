from django.shortcuts import redirect, render
from .models import bb

def index(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/index.html')

def bb(request):
    bb = bb.objects.filter(price__lte = 500).order_by('-price')
    print(str(len(bb)))
    return render(request, 'bbmodule/bbList.html', {'bb': bb})

def filterbb(request):
    
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isPrice = request.POST.get('option1')
        isBridemaid = request.POST.get('option2')
        
        selected = request.POST.get('selectedchoice')
        
        mybb = bb.objects.filter(title__icontains='or')
        mybb2 = mybb.filter(price__lte = 500).exclude(Bridemaid_icontains = 'Sara fahad')
        
        print(f"selected thing = {selected}")
        # now filter
        bb = __getbb() # type: ignore
        newbb = []
        for item in bb:
            contained = False
            if isPrice and string in item['Price'].lower(): contained = True
            if not contained and isBridemaid and string in item['Bridemaid'].lower(): contained = True
            if contained: newbb.append(item)       
        return render(request, 'bbmodule/bbList.html', {'bb':newbb})
    return render(request, 'bbmodule/search.html', {})

def bb(request, bId):
    
    bb1 = {'id':101, 'Makeup artist':'Haifa khaled', 'Price':'1500 SAR'}
    bb2 = {'id':102, 'Makeup artist':'Nourah mohammed', 'Price':'2000 SAR'}
    bb3 = {'id':1011, 'Hair stylist':'Rajwa Alfahad', 'Price':'500-990 SAR'}
    bb4 = {'id':1012, 'Photographer':'Rahaf hamad', 'Price':'5000-10000 SAR'}
    bb5 = {'id':10123, 'Bridemaid':'Maha Ali', 'Price':'1000 SAR /5 hourse'}

    targetbb = None
    if bb1['id'] == bId: targetbb = bb1
    if bb2['id'] == bId: targetbb = bb2
    if bb3['id'] == bId: targetbb = bb3
    if bb4['id'] == bId: targetbb = bb4
    if bb5['id'] == bId: targetbb = bb5
    
    if targetbb == None: return redirect('/bb')
    
    context = {'bb':targetbb} # bb is the variable name accessible by template
    return render(request, 'bbmodule/bb.html', context)
    