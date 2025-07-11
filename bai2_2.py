# main.py

import quy_doi

def main():
    try:
        so_dam = int(input("Nhập số dặm bay: "))
        tien_vnd_moi_dam = int(input("Nhập số tiền VND cho mỗi dặm bay: "))
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    tong_tien_vnd = so_dam * tien_vnd_moi_dam

    print(f"\nTổng tiền (VNĐ): {tong_tien_vnd:,} VND")

    print("Tương đương:")
    print(f"- USD: {quy_doi.doi_sang_usd(tong_tien_vnd):,.2f}")
    print(f"- EUR: {quy_doi.doi_sang_eur(tong_tien_vnd):,.2f}")
    print(f"- JPY: {quy_doi.doi_sang_jpy(tong_tien_vnd):,.2f}")

if __name__ == "__main__":
    main()
