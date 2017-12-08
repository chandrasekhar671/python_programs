Student_list = {'raja':701,'teja':702,'suraj':770,'eswar':780,'bhaskar':990,'chaitu':870,'nani':760,'pavan':775,'reddy':890,'lohith':891}
lab_system_details = {'MCA Lab':{'1':['Free','Good'],'2':['Free','Repair'],'3':['Free','Good'],'4':['Free','Good'],'5':['Free','Good'],'6':['Free','Good'],'7':['Free','Repair'],'8':['Allocated','Good'],'9':['Allocated','Good'],'10':['Allocated','Good']},'Cisco Lab':{'1':['Free','Good'],'2':['Free','Repair'],'3':['Free','Good'],'4':['Allocated','Good'],'5':['Free','Good'],'6':['Allocated','Good'],'7':['Free','Good'],'8':['Free','Good'],'9':['Allocated','Good'],'10':['Free','Good']}}

def get_list_of_free_systems(lab_name):
  #global lab_system_details
  free_system = []
  if lab_name in lab_system_details.keys():
      lab_systems = lab_system_details[lab_name]
      for system_id in lab_systems.keys():
          if lab_systems[system_id][0] == 'Free':
            if lab_systems[system_id][1] == 'Good':
              free_system.append(system_id)

  return free_system

def get_list_of_good_systems(lab_name):
  #global lab_system_details
  good_system = []
  if lab_name in lab_system_details.keys():
    lab_systems = lab_system_details[lab_name]
    for system_id in lab_systems.keys():
        if lab_systems[system_id][1] == 'Good':
          if lab_systems[system_id][0] == 'Free':
            good_system.append(system_id)

  return good_system

mca = get_list_of_free_systems('MCA Lab')
cisco = get_list_of_good_systems('Cisco Lab')
new = mca + cisco
#Student_list = {'Raja':701,'Teja':702,'Suraj':770,'chandra':880}
h = []
g = []
for x,y in Student_list.items():
   h.append(x)
   g.append(y)
for i in range(len(mca)):
  print(h[i] + " - "+ str(g[i]) + " - " + list(lab_system_details.keys())[0] + " - " + str(new[i]))
for i in range(len(mca),len(Student_list)):
  print(h[i] + " - " + str(g[i]) + " - " + list(lab_system_details.keys())[1] + " - " + str(new[i]))
    
    
  
  
  
  