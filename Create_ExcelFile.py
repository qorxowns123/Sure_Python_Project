import xlsxwriter

def create_xls():
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
    worksheet.set_column(2, 7, 20)

    # 셀 병합을 통한 셀 작성
    worksheet.merge_range('A1:B1', '주 차', merge_format)
    worksheet.merge_range('A2:B2', '지출항목', merge_format)
    worksheet.merge_range('A13:B13', '총비용', merge_format)
    worksheet.merge_range('I1:K2', '항목별 총액', merge_format)
    worksheet.merge_range('C1:E1', '', merge_format)
    worksheet.merge_range('F1:H1', '', merge_format)

    for loophdx in range(3, 14):
        start_cell = 'I' + str(loophdx)
        end_cell = 'K' + str(loophdx)
        cell_range = start_cell+':'+end_cell
        worksheet.merge_range(cell_range, '', merge_format)
    
    # 병합이 아닌 셀 작성
    item_list = ['파견지식대', '교통비', '주차비,톨비', '차량유류비', '통신비(우편비)', '운반비(퀵비)', '파견지다과비', '회의비', '인쇄비', '기타']
    for loopidx in range(0, item_list.__len__()):
        worksheet.write(loopidx + 2, 0, loopidx+1, cell_format)
        worksheet.write(loopidx + 2, 1, item_list[loopidx], cell_format)

    menu_list = ['금액', '날짜/횟수', '내역']
    for loopjdx in range(0, 2): # 나중에 이쪽 반복문을 고쳐야 할듯
        for loopkdx in range(0, menu_list.__len__()):
            if loopjdx == 0:
                worksheet.write(1, loopkdx + 2, menu_list[loopkdx], cell_format)
            else:
                worksheet.write(1, loopkdx + 5, menu_list[loopkdx], cell_format)

    workbook.close()

# 메인
if __name__  == "__main__":
    create_xls()