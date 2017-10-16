import xlsxwriter

# store_over_work_day, store_over_work_time, store_over_work_money
def create_xlsx(store_over_work_day, store_over_work_time, store_over_work_money):

    over_work_day_list = store_over_work_day
    over_work_day_time = store_over_work_time
    over_work_day_money = store_over_work_money

    loop_week = over_work_day_list.__len__()

    # 워크북 생성
    workbook = xlsxwriter.Workbook('경비보고서.xlsx')
    # 시트 생성
    worksheet = workbook.add_worksheet('경비보고서')
    # 포맷설정
    merge_format = workbook.add_format({
        'border': 1, # 테두리 스타일
        'bold': 'True', # 굵게
        'align': 'center', # 텍스트 세로 위치
        'valign': 'vcenter' # 텍스트 가로 위치
    })
    cell_format = workbook.add_format({
        'border': 1, # 테두리 스타일
        'align': 'center',  # 텍스트 세로 위치
        'valign': 'vcenter'  # 텍스트 가로 위치
    })

    # column 폭 지정
    worksheet.set_column(1, 1, 14)
    '''
    worksheet.set_column(2, 7, 20)
    '''

    # 셀 병합을 통한 셀 작성
    worksheet.merge_range('A1:B1', '주 차', merge_format)
    worksheet.merge_range('A2:B2', '지출항목', merge_format)
    worksheet.merge_range('A13:B13', '총비용', merge_format)
    
    # 병합이 아닌 셀 작성
    item_list = ['파견지식대', '교통비', '주차비,톨비', '차량유류비', '통신비(우편비)', '운반비(퀵비)', '파견지다과비', '회의비', '인쇄비', '기타']
    for loopidx in range(0, item_list.__len__()):
        worksheet.write(loopidx + 2, 0, loopidx+1, cell_format)
        worksheet.write(loopidx + 2, 1, item_list[loopidx], cell_format)

    # 산출된 주차 수 만큼 금액, 날짜, 내역 출력
    menu_list = ['금액', '날짜/횟수', '내역']
    first_col = -1
    last_col = 1
    for loopjdx in range(0, loop_week):
        first_col = first_col + 3
        last_col = last_col + 3 # end point
        worksheet.merge_range(0, first_col, 0, last_col, over_work_day_list[loopjdx][0], merge_format)
        worksheet.set_column(first_col, last_col, 20)
        for loopcdx in range(1, 13):
            for loopkdx in range(0, menu_list.__len__()):
                if loopcdx == 1:
                    worksheet.write(loopcdx, first_col + loopkdx, menu_list[loopkdx], cell_format)
                elif loopcdx == 3:
                    for loopadx in range(1 , over_work_day_list[loopjdx].__len__()):
                        worksheet.write(loopcdx, first_col, over_work_day_money[loopjdx][loopadx], cell_format)
                        worksheet.write(loopcdx, first_col+1, over_work_day_time[loopjdx][loopadx], cell_format)
                        worksheet.write(loopcdx, last_col, '야근교통비', cell_format)
                else:
                    worksheet.write(loopcdx, first_col + loopkdx, '', cell_format)

    # 항목별 총액
    worksheet.merge_range(0, last_col + 1, 1, last_col + 2, '항목별 총액', merge_format)
    for loopbdx in range(2, 13):
        worksheet.merge_range(loopbdx, last_col + 1, loopbdx, last_col + 2, '', merge_format)

    # 워크북 종료
    workbook.close()
    print('Excel 생성 완료...')

'''
# 메인
if __name__  == "__main__":
    list = ['1주차']
    dict = {'day':'월', '시간':'10시'}
    list.append(dict)
    print(list)
    dict = []
    list.append(dict)
    print(list)
'''