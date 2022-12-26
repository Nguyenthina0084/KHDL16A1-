# Quản lý lương nhân viên
import os, csv

#from csv import reader
_path="files/ds_luongnv.csv"
lstLuongNv=[]
#--------Hàm thứ nhất-----------------------------------------------------
def mo_file_luong_nhan_vien(_path,lstLuongNv):
    try:
        f=open(_path,'r', encoding ='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='so_ds':
                continue
            lstLuongNv.append({'so_hs':dong[0],'so_nv':dong[1], 'ho_tennv':dong[2],'luong_ngay':dong[3],'Ngay_cong':dong[4],\
                'luong_thang':dong[5],'thuong':dong[6]})
        f.close()
        return 1
    except Exception as ex1:
        print('Khong mở được file hop le ', ex1)
    return
#--------Hàm thứ hai---------------------------------------------------
def luu_ds_luong_nhan_vien(_path,lstLuongNv):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['so_ds','ho_tennv','luong_ngay','Ngay_cong','luong_thang','thuong'])
        for nv in lstLuongNv:
            csv.writer(f).writerow([nv['so_ds'],nv['ho_tennv'],nv['luong_ngay'],nv['ngay_cong'],\
            nv['luong_thang'],nv['thuong']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
#--------Hàm thứ ba-----------------------------------------------------
def them_ds_nhan_vien(lstLuongNv):
    while True:
        so_ds=input('Nhập số nhân viên: ')
        ho_tennv=input('Họ tên nhân viên: ')
        Ngay_cong=float(input('Ngày công của nhân viên: '))
        luong_ngay=float(input('Lương ngày của nhân viên:'))
        thuong=float(input('Thưởng: '))
        Luong_thang=input(Ngay_cong*luong_ngay+thuong)
        
        lstLuongNv.append({'so_ds':so_ds,'luong_ngay':luong_ngay,\
             'ho_tennv':ho_tennv,'Ngay_cong':Ngay_cong,'luong_ngay':luong_ngay,\
        'thuong':thuong,'luong_thang':Luong_thang})
        #Hết lệnh append    
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
    return   
#----------------------------------------------------------------------------------
def in_ds_luong_nhan_vien(lstLuongNv):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_ds','luong_ngay',\
         'ho_tennv','Ngay_cong','luong_ngay',\
        'dien_thoai','tong_tien_hd','tam_ung','con_lai'))
    
    for hd in lstLuongNv:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],\
            hd['ngay_hd'], hd['ho_tenkh'],hd['dia_chi'],hd['quan'],\
        hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))

    return
#---------------------------------------------------------------------------------
def tra_cuu_luong_nhan_vien(lstLuongNv):
    for ds in lstLuongNv:
        if ds['so_ds']==sods:
            return ds
    return
#-------Hàm thống kê (thong_ke()), cho phép thống kê tổng tiền, tạm ứng, Tiền còn lại của tất cả hóa đơn.
def thong_ke(lstLuongNv):
    tong=0
    tong_thuong=0
    lstthongke=[]
    for ds in lstLuongNv:
            tong+=float(ds['luong_thang'])
            tong_tamung+=float(ds['thuong'])
    tong_tien_luong=float(tong+tong_thuong)
    print('Tổng tiền tất cả các hóa đơn: %f'%tong)
    print('Tổng tiền tạm ứng tất cả các hóa đơn: %f'%tong_thuong)
    print('Tổng tiền còn lại của tất cả các hóa đơn: %f'%tong_tien_luong)
    return 
def xoa_ds_nhân_viên(lstLuongNv):
    for i in range(len(lstLuongNv)):
        ds=lstLuongNv[i]
        if ds['so_hd']==sods:
            del(lstLuongNv[i])
            return 1
    return 0
#----------------------------------------------------------------------------------
#sắp xếp hóa đơn theo thứ tự giảm dần của tổng tiền hợp đồng
def sapxep(lstLuongNv):
    luong_nv = sorted(lstLuongNv, key=lambda x: x['tong_tien_luong'])
    
    return luong_nv
#----------------------------------------------------------------------------------

#------------BẮT ĐẦU CHƯƠNG TRÌNH-------------------------------
print('CHƯƠNG TRÌNH QUẢN LÝ LƯƠNG NHÂN VIÊN')
print('Được viết by nhóm 8.THÀNH VIÊN GỒM:Nguyễn thị Na .....xyz.....ngày viết26/12/2022')
while True:
    print('1: Thêm ds nhân viên')
    print('2: Danh sách lương nhân viên')
    print('3: Tra cứu lương nhân viên')
    print('4: Xóa ds lương nhân viên')
    print('5: Thống kê')
    print('6: Sắp xếp')
    print('7: Lưu danh sách hóa đơn ra file CSV')
    print('8: Đọc file CSV')
   
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon ==1:
        them_ds_nhan_vien(lstLuongNv)
    elif chon==2:
        in_ds_luong_nhan_vien(lstLuongNv)
    elif chon==3:
        sods=input('Nhập số hóa đơn cần tra cứu')
        ds=tra_cuu_luong_nhan_vien(lstLuongNv,sods)
        if ds==None:
            print("Không tra cứu được số hóa đơn %d"%sods)
        else:
            print(ds)
    elif chon==4:
        sods=input('Nhập số hóa đơn cần xóa: ')
        kt=input('Bạn có chắc chắn muốn xóa không? (c/C hay k/K?')
        if kt =='c' or kt =='C':
            kq=xoa_ds_nhân_viên(lstLuongNv,sods)
            if kq==1:
                print('Đã xóa nhân viên số ',sods)
            else:
                print('Không tồn tại số nhân viên bạn muốn xóa')
    elif chon==5:
        thong_ke(lstLuongNv)   
   
    elif chon==6:
        print("Danh sách trước khi sắp xếp theo tổng tiền là:",in_ds_luong_nhan_vien(lstLuongNv))   
        #sap_xep(lstHoaDon)
        print("Danh sách sau khi sắp xếp theo tổng tiền là:",in_ds_luong_nhan_vien(lstLuongNv))     
    elif chon==7:
        if luu_ds_luong_nhan_vien(_path, lstLuongNv)==1:
            print('Lưu thành công !')
        else:
            print('Không lưu được !!!')
        luu_ds_luong_nhan_vien(_path, lstLuongNv) 
    elif chon==8:
        if mo_file_luong_nhan_vien(_path,lstLuongNv):
            print("Đã đọc được file vào lstLuongNv ")
    else:
        break
    
    tt=input('Bạn có muốn tiếp tục (1:tt) ')
    
    if tt!='1':
        break
    else: 
        os.system('cls')
    input('Gõ phím bất kỳ để tiếp tục chương trình !!!')    