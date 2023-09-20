from contextlib import closing

from django.db import connection
from methodism import dictfetchall

from app.models import Service
from django.shortcuts import render,redirect

def client_doc(request,service:int = None):
    sql=f"""
    select cr.id as cr_id, cr.name as cr_name, doc.id, doc.name as fname, doc.familya as lname, doc.img,doc.phone,doc.gender  
    from app_service as cr
    inner join app_servicedoc sd on sd.service_id=cr.id
    inner join app_user doc on sd.doc_id=doc.id
    where cr.id={service}
    
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
    print(result,'==================')
    ctx = {
        "roots" : result,
    }

    return render(request,'page/client/client_doc.html',ctx)
