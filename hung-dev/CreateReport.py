import glob
from utils import *
import darshan
import pandas as pd

fopInput='/home/hungphd/git/aiio/darshan-logs-for-paper/'
fopOutputHtml= '/home/hungphd/git/aiio/darshan-logs-for-paper-html/'
fopOutputXlsx= '/home/hungphd/git/aiio/darshan-logs-for-paper-xlsx/'
createDirIfNotExist(fopOutputHtml)
createDirIfNotExist(fopOutputXlsx)

lstFpDarshans=glob.glob(fopInput+'*.darshan')
lstStr=[]
for fpItem in lstFpDarshans:
    arrFp=fpItem.split('/')
    nameHtml=arrFp[len(arrFp)-1].replace('.darshan','.html')
    nameXlsx = arrFp[len(arrFp) - 1].replace('.darshan', '.xlsx')
    strCommand='python -m darshan summary {} --output {}'.format(fpItem, fopOutputHtml + nameHtml)
    lstStr.append(strCommand)

    with darshan.DarshanReport(fpItem, read_all=True) as report:
        # print the metadata dict for this log
        print("metadata: ", report.metadata)
        # print job runtime and nprocs
        print("run_time: ", report.metadata['job']['run_time'])
        print("nprocs: ", report.metadata['job']['nprocs'])

        # print modules contained in the report
        print("modules: ", list(report.modules.keys()))
        lstModuleNames=list(report.modules.keys())
        lstDfs=[]
        # writer = pd.ExcelWriter(fopOutputXlsx + nameXlsx, engine="xlsxwriter")
        # for moduleName in lstModuleNames:
        #     try:
        #         df = report.records[moduleName].to_df()
        #         if isinstance(df,dict):
        #             print('type {}'.format(type(df['counters'])))
        #             print(df)
        #             # dfCounters = df['counters']
        #             for key in df.keys():
        #                 df[key].to_excel(writer, sheet_name='{}_{}'.format(moduleName,key))
        #     except Exception as e:
        #         traceback.print_exc()
        #
        # writer.close()

        # # export POSIX module records to DataFrame and print
        posix_df = report.records['APMPI'].to_df()
        print("POSIX df: ", posix_df)


f1=open(fopOutputHtml + 'a_genHtml.sh', 'w')
f1.write('\n'.join(lstStr))
f1.close()
