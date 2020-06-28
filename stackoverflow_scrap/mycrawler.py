# Importing functions from custom made file
from scrapfunc import(
    get_urldata,
    get_urldata_wh,
    get_tagdata
)  

#------------------------------------------------------------------#
# This program scrap top searched tags from stackoverflow website,
# also their Questions count 
#------------------------------------------------------------------#

tag_title = []
Q_count = []

for i in range(1,2):
    soup = get_urldata('https://stackoverflow.com/tags?page='+ str(i) +'&tab=popular', 'lxml')
    data = get_tagdata(soup, 'a', 'post-tag')
    #data1 = get_tagdata(soup, 'div', 'mt-auto grid jc-space-between fs-caption fc-black-300')
    tag_title.append(data)
    #Q_count.append(data1)

#Q_count1 = Q_count[0]+Q_count[1]
#tag_title1 = tag_title[0]+tag_title[1]+tag_title[2]+tag_title[3]
print(tag_title)
