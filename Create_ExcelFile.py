import xlsxwriter

# store_over_work_day, store_over_work_time, store_over_work_money
class CreateExcelFile:
    def create_xlsx(self, TimetoMoneyList, set_day_info):

        get_year = set_day_info[0]
        get_month = set_day_info[1]
        filename = get_year + '_' + get_month + '_' + '경비보고서.xlsx'

        # 워크북 생성
        workbook = xlsxwriter.Workbook(filename)
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
            'valign': 'vcenter',  # 텍스트 가로 위치
            'text_wrap': True
        })

        numric_format = workbook.add_format({
            'border': 1,  # 테두리 스타일
            'align': 'center',  # 텍스트 세로 위치
            'valign': 'vcenter',  # 텍스트 가로 위치
        })
        numric_format.set_num_format('#,##0')

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
        SubFormSetFunc(worksheet, cell_format, merge_format, menu_list, TimetoMoneyList)
        MainFormSetFunc(worksheet, numric_format, cell_format, TimetoMoneyList)
        # A column폭 지정
        worksheet.set_column('A:A', 10)
        # B column폭 지정
        worksheet.set_column('B:B', 17)

        # 워크북 종료
        workbook.close()
        return filename


def MainFormSetFunc(worksheet, numric_format, cell_format, TimetoMoneyList):
    getTotalSum = 0
    first_col = -1
    loop_week = TimetoMoneyList.__len__()
    for loopidx in range(0, loop_week):
        getSum = 0
        if TimetoMoneyList[loopidx].__len__() == 1:
            continue
        else:
            first_col = first_col + 3
            for loopjdx in range(1, TimetoMoneyList[loopidx].__len__()):
                getSum = getSum + TimetoMoneyList[loopidx][loopjdx]
            
            # 금액 총합
            worksheet.write(3, first_col, getSum, numric_format)
            getTotalSum = getTotalSum + getSum
            # 야근 횟수
            cntStr = str((TimetoMoneyList[loopidx].__len__() - 1)) + '회'
            worksheet.write(3, first_col+1, cntStr, cell_format)

    # 항목별 총액
    worksheet.write(3, first_col+3, getTotalSum, numric_format)

def SubFormSetFunc(worksheet, cell_format, merge_format, menu_list, TimetoMoneyList):
    first_col = -1
    last_col = 1
    loop_week = TimetoMoneyList.__len__()
    for loopidx in range(0, loop_week):
        if TimetoMoneyList[loopidx].__len__() == 1:
            continue
        else:
            first_col = first_col + 3
            last_col = last_col + 3
            worksheet.merge_range(0, first_col, 0, last_col, TimetoMoneyList[loopidx][0], merge_format)
            worksheet.set_column(first_col, last_col, 15)
            worksheet.write(1, first_col, menu_list[0], cell_format)
            worksheet.write(1, first_col+1, menu_list[1], cell_format)
            worksheet.write(1, last_col, menu_list[2], cell_format)
            for loopjdx in range(2, 13):
                worksheet.write(loopjdx, first_col, '', cell_format)
                worksheet.write(loopjdx, first_col + 1, '', cell_format)
                worksheet.write(loopjdx, last_col, '', cell_format)

            worksheet.write(0, last_col+1, '항목별 총액', merge_format)
            worksheet.set_column(last_col+1, last_col+1, 20)
            for loopjdx in range(1, 13):
                worksheet.write(loopjdx, last_col+1, '', cell_format)