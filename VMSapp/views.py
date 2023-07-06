from django.shortcuts import render,redirect
from django.views.generic import View
from VMSapp.models import Vms
from VMSapp.forms  import CarCreateForm

class AddCarView(View):
    model=Vms
    form_class=CarCreateForm
    template_name='vehicleadd.html'

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,self.template_name,{'form':form})



class VehicleListView(View):
    model=Vms
    template_class='vehiclelist.html'

    def get(self,request,*args,**kwargs):
        qs=Vms.objects.all()
        return render(request,self.template_class,{'cars':qs})
    


class VehicleDetailView(View):
    template_name='vehicledetail.html'
    model=Vms
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        print(id)
        qs=Vms.objects.get(id=id)
        return render(request,self.template_name,{'cars':qs})

class VehicleUpdate(View):
    model=Vms
    form_class=CarCreateForm
    template_name='vehicleupdate.html'

    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Vms.objects.get(id=id)
        form=CarCreateForm(instance=obj)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Vms.objects.get(id=id)
        form=CarCreateForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,self.template_name,{'form':form})


def deleteVehicleDetail(request,*args,**kwargs):
    id=kwargs.get('pk')
    Vms.objects.filter(id=id).delete()
    return redirect('list')
    