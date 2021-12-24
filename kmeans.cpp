// K Means Algorithm

#include <ctime>     // for a random seed
#include <fstream>   // for file-reading
#include <iostream>  // for stdio
// #include <sstream>   // for file-reading
#include <vector>
#include <cmath>  // for abs

struct Point {
    double x, y;     // coordinates
    int cluster;     // associated cluster
    double minDist;  // distance(2) to nearest cluster

    Point(double x, double y) :
        x(x),
        y(y),
        cluster(-1),
        minDist(__DBL_MAX__) {}

    double dist2(Point p) {
        return (p.x - x) * (p.x - x) + (p.y - y) * (p.y - y);
    }
};


std::vector<Point> getPointsFromCSV(std::string filename) {
 std::vector<Point> points;
 std::string line;
 std::ifstream file(filename);

 double x, y;

 if(file.is_open()){
  while (getline(file,line)){
    //std::cout << line << "\n";

    x = std::stod(line.substr(0 , line.find(",") ));
    y = std::stod(line.substr(line.find(",") + 1));

    // std::cout<<x<<std::endl;
    // std::cout<<y<<std::endl;
    // std::cout<<"---\n";

    points.push_back(Point(x,y));

  }
 }
 return points;
}


void associatePointsToClusters(std::vector<Point>* points, std::vector<Point>* centers)
{

// for each point, find the nearest center

  //std::cout<<"finding points\n";
  int pointnr = 0;
  for (std::vector<Point>::iterator it = points->begin();
       it != points->end(); ++it) {
   
   Point p = *it;
   //std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
   
   int centerid = 0;
   for (std::vector<Point>::iterator c = centers->begin();
        c != centers->end(); ++c) {
    
    double dist = p.dist2(centers->at(centerid));
    //std::cout<<"dist "<<dist<<"\n";
    if(dist < p.minDist){
     p.minDist=dist;
     p.cluster=centerid;
    }
    centerid++;  
   }
   //std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
   points->at(pointnr).minDist = p.minDist; 
   points->at(pointnr).cluster = p.cluster; 
   pointnr++;
  }
}


void initCenters(std::vector<Point>* pointlist, int ncenters, std::vector<Point>* oldcenterlist, std::vector<Point>* newcenterlist){
 //srand(time(0));  // need to set the random seed
 for (int i = 0; i < ncenters; ++i) {
     oldcenterlist->push_back( Point(__DBL_MAX__,__DBL_MAX__) );
     newcenterlist->push_back(pointlist->at(rand() % pointlist->size() ));
     //newcenterlist.push_back(points->at(rand() % points->size() ));
 }
}


void recalculateCenters(std::vector<Point>* points, std::vector<Point>* centers){

std::vector<int> nPoints;
std::vector<double> sumX, sumY;

 // Initialise with zeroes
 for (int i = 0; i < centers->size(); ++i) {
     nPoints.push_back(0);
     sumX.push_back(0.0);
     sumY.push_back(0.0);
 }

 for (std::vector<Point>::iterator it = points->begin();
      it != points->end(); ++it) {
  
  Point p = *it;
  //std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";

  nPoints[p.cluster]++;
  sumX[p.cluster] += p.x;
  sumY[p.cluster] += p.y;

  p.minDist = __DBL_MAX__;

 } 

 int centerid = 0;
 for (std::vector<Point>::iterator c = centers->begin();
      c != centers->end(); ++c) {
  
  std::cout<<" Old Center "<<std::endl;
  std::cout<<centers->at(centerid).x<<","<<centers->at(centerid).y<<"\n";

  //std::cout<<sumX[centerid]<<"\n";
  //std::cout<<sumY[centerid]<<"\n";

  std::cout<<" New Center "<<std::endl;
  centers->at(centerid).x = sumX[centerid]/nPoints[centerid];
  centers->at(centerid).y = sumY[centerid]/nPoints[centerid];
  std::cout<<centers->at(centerid).x<<","<<centers->at(centerid).y<<"\n";

  centerid++;  

 }
  
}


int main()
{

 int ncenters = 2;

 std::string filename = "twoblobs.csv";

 std::vector<Point> pointlist =  getPointsFromCSV(filename);

 std::vector<Point> oldcenterlist;
 std::vector<Point> newcenterlist;
 initCenters(&pointlist, ncenters, &oldcenterlist, &newcenterlist);

 //std::cout<<" Centers init-ed\n";
 //for (int i = 0; i < ncenters; ++i) {
 //  std::cout << newcenterlist[i].x << " " << newcenterlist[i].y <<std::endl;
 //}

 //std::cout<<" Unassociated points\n";
 //for (std::vector<Point>::iterator it = pointlist.begin();
 //     it != pointlist.end(); ++it) {
 // Point p = *it;
 // std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
 //}


 int iterationnr = 0;
 while(true){
  associatePointsToClusters(&pointlist, &newcenterlist);

  //std::cout<<" Associated points\n";
  //for (std::vector<Point>::iterator it = pointlist.begin();
  //     it != pointlist.end(); ++it) {
  // Point p = *it;
  // std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
  // 
  //}

  recalculateCenters(&pointlist, &newcenterlist);

  //std::cout << newcenterlist.size() <<std::endl;
  //for (int i = 0; i < newcenterlist.size(); ++i) {
  //  std::cout << newcenterlist[i].x << " " << newcenterlist[i].y <<std::endl;
  //}

  double diffX = 0;
  double diffY = 0;
  for (int i = 0; i < newcenterlist.size(); ++i) {
    diffX += newcenterlist[i].x - oldcenterlist[i].x;
    diffY += newcenterlist[i].y - oldcenterlist[i].y;
  }
  std::cout<<" Diffs "<<diffX<<" "<<diffY<<"\n";
  std::cout<<std::abs(diffX+diffY)<<"\n";

  //write to file
  std::ofstream myfile;
  std::string filename = "outfile"+std::to_string(iterationnr)+".csv";
  myfile.open(filename);
  myfile << "x,y,c" << std::endl;
  
  for (std::vector<Point>::iterator it = pointlist.begin(); 
       it != pointlist.end(); ++it) {
      myfile << it->x << "," << it->y << "," << it->cluster << std::endl;
  }
  myfile.close();


  if(std::abs(diffX+diffY) < 0.1) break;

  for (int i = 0; i < newcenterlist.size(); ++i) {
    oldcenterlist[i].x = newcenterlist[i].x;
    oldcenterlist[i].y = newcenterlist[i].y;
  }
  
 iterationnr++;

 }

}

