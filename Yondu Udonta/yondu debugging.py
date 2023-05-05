def main():
    reavers = 30
    units = 3000
    shore_cut = 3
    units_after_cut = units - ((reavers - 2) * shore_cut)
    print(f"units after shore cut {units_after_cut}")
    
    yondu_share = int(units_after_cut * .13)
    units_after_cut -= yondu_share
    print(f"units after yondu cut {units_after_cut}")
    
    quill_share = int(units_after_cut * .11)
    units_after_cut -= quill_share
    print(f"units after quill cut {units_after_cut}")
    
    crew_share = int(units_after_cut * (1 / reavers))
    rbf_donation = int(units_after_cut % reavers)
    print(f"crew share {crew_share}")
    print(f"rbf donation {rbf_donation}")
    print(int(yondu_share) + int(quill_share) + int((crew_share) * reavers) + int(rbf_donation))
main()
    
    
    
    