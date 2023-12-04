import datetime
from functions import get_vna, get_pu

case_testes = [
  { "data_selected": "10/11/2023", "due_date": "15/08/2028", "taxa": 0.07 , "vna": 4158.526771, "pu": 4057.927849},
  { "data_selected": "11/11/2023", "due_date": "15/08/2028", "taxa": 0.07 , "vna": 4159.001442, "pu": 4059.480696},
  { "data_selected": "22/11/2023", "due_date": "15/08/2028", "taxa": 0.07 , "vna": 4162.246133, "pu": 4069.194958},
  { "data_selected": "10/10/2023", "due_date": "15/08/2040", "taxa": 0.07 , "vna": 4150.483805, "pu": 3797.925108},
  { "data_selected": "01/12/2023", "due_date": "15/05/2035", "taxa": 0.07 , "vna": 4166.265754, "pu": 3868.281928},
  { "data_selected": "29/11/2023", "due_date": "15/05/2035", "taxa": 0.07 , "vna": 4165.116895, "pu": 3865.141011},
  { "data_selected": "04/12/2023", "due_date": "15/05/2035", "taxa": 0.07 , "vna": 4166.840303, "pu": 3869.852927}
]

for case_sim in case_testes:
  data_selected_string = case_sim['data_selected']
  selected_date = datetime.datetime.strptime(data_selected_string, "%d/%m/%Y")

  due_date_string = case_sim['due_date']
  due_date = datetime.datetime.strptime(due_date_string, "%d/%m/%Y")

  vna = get_vna(data_selected_string)
  assert vna == case_sim['vna'], f"expected VNA: {case_sim['vna']}, got VNA: {vna}, on: {data_selected_string}"

  taxa = 0.07
  pu = get_pu(vna, selected_date, due_date, taxa)
  assert pu == case_sim['pu'], f"expected PU: {case_sim['pu']}, got PU: {pu}, on: {data_selected_string}"

  print("VNA: ", vna, " PU: ", pu, " DATA_SELECTED: ", data_selected_string, " DUE_DATE: ", due_date_string)