import sys

NAND_PAGE_SIZE = 0x800 # 2048 bytes
NAND_PAGE_BLK = 64 # 64 pages per block
NAND_SECTOR_PER_PAGE = 4 # 4 sectors in page
NAND_SECTOR_SIZE = NAND_PAGE_SIZE/NAND_SECTOR_PER_PAGE
OOBLEN = 64

inf = open(sys.argv[1] , "rb")
of = open(sys.argv[2], "wb")

def page2off(pgno):
    return pgno * 0x840 # (NAND_PAGE_SIZE + NAND_SECTOR_PER_PAGE*OOBLEN)

def read_page(inf, blkno, pgno):
    blklen = page2off(NAND_PAGE_BLK)
    fileoff = blklen * blkno + page2off(pgno)

    print "reading block %d page %d: offset %08X" % (blkno, pgno, fileoff)

    inf.seek(fileoff, 0)
    block = inf.read(blklen)
    buf = ""

    for i in range(NAND_PAGE_SIZE):
        buf += block[i]

   return s

for blkn in range(1024):
    for pagen in range(64):
        res = read_page(inf, blkn, pagen)
        of.write(res)