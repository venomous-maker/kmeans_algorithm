def get_point():
  val_x, val_y = input("Enter the value of X and Y repectively separated by space: ").split()
  try:
    val_x, val_y = float(val_x),float(val_y)
    my_tuple = (val_x, val_y)
  except:
    my_tuple = (0.0, 0.0)
    print("An Error occurred")
  return my_tuple

def dist(my_tuple1=(1.0,0.0),my_tuple2=(0.0,1.0)):
  diffs = [my_tuple1[x] - my_tuple2[x] for x in range(len(my_tuple1))]
  diff_squared = [diff ** 2 for diff in diffs]
  total_for_squares = sum(diff_squared)
  root = total_for_squares ** 0.5
  return root

def centroid(list_of_list=[[0.0,0.0]]):
  sum_x = 0.0
  sum_y = 0.0
  for i in range(len(list_of_list)):
    sum_x += list_of_list[i][0]
    sum_y += list_of_list[i][1]
  total = len(list_of_list)
  average_x = sum_x/total
  average_y = sum_y/total
  returned_tuple = (average_x,average_y)
  return returned_tuple

def assign_cluster(list_of_centroids = [(1.0,0.0),(0.0,1.0)], list_of_data_points = [[0.0,1.0]]):
  cluster = []
  for j in range(len(list_of_centroids)):
    euc_dist = []
    for i in range(len(list_of_data_points)):
      euc_dist.append(dist(list_of_centroids[j],tuple(list_of_data_points[i])))
    min = euc_dist[0]
    min_ind = 0
    for m in range(len(euc_dist)):
      if euc_dist[m] < min:
        min = euc_dist[m]
        min_ind = m
    cluster.append(min_ind)
  return cluster

def main(centroids = 2):
  list_of_list1 =[]
  data_points = input("Enter the data points to cluster: ")
  try:
    data_points = int(data_points)
    for i in range(data_points):
      tuple_out = get_point()
      X, Y = tuple_out[0],tuple_out[1]
      list_of_list1.append([X,Y])
    
    centroid_turple = []
    for i in range(centroids):
      print(f"Centroid {i+1}:")
      centroid_turple.append(get_point())
    
    clusters = assign_cluster([turple for turple in centroid_turple],list_of_list1)
    for i in range(len(clusters)):
      print(f"Iteration {i+1}")

      for j in range(len(clusters)):
        if j==0:
          cluster_s = list_of_list1[:(clusters[i]+1)]
        else:
          cluster_s = list_of_list1[clusters[i]+1:]

        new_centroid = centroid(cluster_s)
        print(f"Clusters {j+1}: {cluster_s }")
        print(f"New Centroid: {new_centroid}\n")
    print('Done')
  except:
    print("An error occurred")

if __name__ == "__main__":
  main(centroids=4)
