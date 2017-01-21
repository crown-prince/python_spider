from bs4 import BeautifulSoup

html = """
<table>
    <tr>
        <td>船名</td>
        <td>航次</td>
        <td>提单号</td>
        <td>箱号</td>
        <td>报关单号</td>
        <td>作业码头</td>
        <td>海关放行状态</td>
        <td>EDI中心接收时间</td>
        <td>序列号</td>
    </tr>
    <tr>
        <td>CSCL OSAKA</td>
        <td>8197W</td>
        <td>KTSNSHA9AA003</td>
        <td>CSLU1106216</td>
        <td>220120161011282136</td>
        <td>外二期</td>
        <td>已放行</td>
        <td>201611161013</td>
        <td>400094490047</td>
    </tr>
    <tr>
        <td>CSCL OSAKA</td>
        <td>8197W</td>
        <td>KTSNSHA9AA003</td>
        <td>CSLU1374965</td>
        <td>220120161011282136</td>
        <td>外二期</td>
        <td>已放行</td>
        <td>201611161013</td>
        <td>400094490047</td>
    </tr>
</table>
"""
soup = BeautifulSoup(html, 'html.parser')
data_list = []  # 结构: [dict1, dict2, ...], dict结构{'船名': ship_name, '航次': voyage, '提单号': bill_num, '作业码头': wharf}
for idx, tr in enumerate(soup.find_all('tr')):
    if idx != 0: #剔除了第一行：{'航次': '航次', '作业码头': '作业码头', '提单号': '提单号', '船名': '船名'}
        tds = tr.find_all('td')
        data_list.append({
            '船名': tds[0].contents[0],
            '航次': tds[1].contents[0],
            '提单号': tds[2].contents[0],
            '作业码头': tds[5].contents[0]
        })
for i in data_list:
    print(str(i) + "\n")
