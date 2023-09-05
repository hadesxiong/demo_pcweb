# codingt=utf8
from rest_framework.decorators import api_view

from django.db.models import Subquery
from django.http.response import JsonResponse

from kpi_server.models import Org,IndexDetail
from kpi_server.serializers import RankSingleSerializer

import datetime

'''获取单项排行'''
@api_view(['GET'])
def getSingleRank(request):

    # params解析
    query_params = {
        'index_num':request.query_params.get('index',None),
        'rank_type':request.query_params.get('type',None),
        'rank_target':request.query_params.get('target',None),
        'data_date': request.query_params.get('date',None)
    }

    # 判断空参数
    if None in query_params.values():
        re_msg = {'code':1,'msg':'err params.'}

    elif query_params['rank_type'] != 'histroy':

        # 日期处理
        # 获取计划筛选日期
        this_year = int(query_params['data_date'].split('-')[0])
        last_year = this_year -1

        fd_ty = datetime.date(this_year,1,1).strftime("%Y-%m-%d")
        ld_ly = datetime.date(last_year,12,31).strftime("%Y-%m-%d")

        # '''single模式 - 获取战客/区域中心/单点的排行'''

        if query_params['rank_type'] == 'single':

            # 机构筛选条件
            org_queryset = Org.objects.filter(org_group=int(query_params['rank_target']))
            if query_params['rank_target'] == '1':
                org_queryset = org_queryset.filter(org_level=3)

        # '''belong模式 - 获取下属机构排行'''
        elif query_params['rank_type'] == 'belong': 
            
            # 机构筛选条件
            org_queryset = Org.objects.filter(parent_org_id=query_params['rank_target'])
        
        # 数据筛选 - 本月完成
        tm_done_queryset = IndexDetail.objects.filter(
            index_num=query_params['index_num'],
            detail_date=query_params['data_date'],
            detail_type=2,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).values('index_num','detail_belong','detail_value')

        # 数据筛选 - 本年计划
        ty_plan_queryset = IndexDetail.objects.filter(
            index_num=query_params['index_num'],
            detail_date=fd_ty,
            detail_type=1,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).values('index_num','detail_belong','detail_value')

        # 数据筛选 - 上年期末
        ly_done_queryset = IndexDetail.objects.filter(
            index_num=query_params['index_num'],
            detail_date=ld_ly,
            detail_type=2,
            detail_belong__in=Subquery(org_queryset.values('org_num'))
        ).values('index_num','detail_belong','detail_value')

        rank_data = []

        for tm,ty,ly in zip(tm_done_queryset,ty_plan_queryset,ly_done_queryset):
            detail_belong = tm['detail_belong']
            value_tm_done = tm['detail_value']
            value_ly_done = ly['detail_value']
            value_compare = tm['detail_value'] - ly['detail_value']
            value_ty_plan = ty['detail_value']
            value_rate = round(tm['detail_value']/ty['detail_value']*100,2)

            rank_data.append({
                'detail_belong':detail_belong,'value_tm_done':value_tm_done,'value_ly_done':value_ly_done,
                'value_compare':value_compare,'value_ty_plan':value_ty_plan,'value_rate':value_rate
            })

        result = RankSingleSerializer(rank_data,many=True).data

        re_msg = {'data':result,'code':0}

    else:

        # 机构筛选
        org_queryset = Org.objects.filter(org_num=query_params['rank_target'])

        # 处理日期
        


    return JsonResponse(re_msg,safe=False)