// K Means Algorithm

#include <ctime>     // for a random seed
#include <fstream>   // for file-reading
#include <iostream>  // for stdio
#include <vector>
#include <cmath>     // for abs
#include <limits>    // for initializing to max/min

struct Point {
    double x, y;                // coordinates
    std::vector<int> cluster;   // associated cluster(s)
    double minDist;             // distance(2) to nearest cluster

    Point(double x, double y) :
        x(x),
        y(y) {}
        //cluster(-1),
        //minDist(__DBL_MAX__) {}

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

void findRangeOfInputData( float& minX, float& minY,
                           float& maxX, float& maxY,
                           std::vector<Point>& pointlist ){


  // std::cout<<" Before doing anything\n";
  // std::cout<<maxX<<" "<<maxY<<"\n";
  // std::cout<<minX<<" "<<minY<<"\n";

  for (std::vector<Point>::iterator it = pointlist.begin();
       it != pointlist.end(); ++it) {
   Point p = *it;
   //std::cout<<"("<<p.x<<","<<p.y<<")"<<"\n";
   if( p.x < minX) minX = p.x;
   if( p.x > maxX) maxX = p.x;
   if( p.y < minY) minY = p.y;
   if( p.y > maxY) maxY = p.y;
  }

  // std::cout<<" After looking through points\n";
  // std::cout<<maxX<<" "<<maxY<<"\n";
  // std::cout<<minX<<" "<<minY<<"\n";

}


void initializeCenters( const int& ncentersX, const int& ncentersY,
                        const float& minX,    const float& minY,
                        const float& maxX,    const float& maxY,
                        std::vector<Point>& centerlist ){

 std::vector<float> xs;
 std::vector<float> ys;

 float xdiff = maxX - minX;
 float xinc = xdiff/(ncentersX-1);
 float ydiff = maxY - minY;
 float yinc = ydiff/(ncentersY-1);

 for( int i=0; i<ncentersX; ++i){
  xs.push_back( minX + i*xinc );
 }

 for( int i=0; i<ncentersY; ++i){
  ys.push_back( minY + i*yinc );
 }

 for (std::vector<float>::iterator itX = xs.begin();
      itX != xs.end(); ++itX) {
  for (std::vector<float>::iterator itY = ys.begin();
       itY != ys.end(); ++itY) {
   centerlist.push_back( Point( *itX, *itY ) );
  }
 }

}


void associateCentersToPoints( std::vector<Point>& pointlist,
     std::vector<Point>& centerlist, float searchradius ){

 // for each point, see if center_i is within searchradius
 // if so, add it to the list
 int pointnr = 0;
 int centernr = 0;
 for (std::vector<Point>::iterator itPoint = pointlist.begin();
      itPoint != pointlist.end(); ++itPoint) {
  for (std::vector<Point>::iterator itCenter = centerlist.begin();
       itCenter != centerlist.end(); ++itCenter) {

  std::cout<<"Point:  ("<<itPoint->x<<","<<itPoint->y<<")\n";
  std::cout<<"Center: ("<<itCenter->x<<","<<itCenter->y<<")\n\n";
  if( itPoint->dist2(*itCenter) < searchradius*searchradius )
   pointlist.at(pointnr).cluster.push_back( centernr );
   // std::cout<<pointlist.at(pointnr).x<<" "<<pointlist.at(pointnr).y<<"\n\n";
   // std::cout<<centerlist.at(centernr).x<<" "<<centerlist.at(centernr).y<<"\n\n";
 
  centernr++;
  }
 centernr = 0;
 pointnr++;
 }

}


 //  //  void associatePointsToClusters(std::vector<Point>* points, std::vector<Point>* centers)
 //  //  {
 //  //  
 //  //   // for each point, find the nearest center
 //  //  
 //  //   //std::cout<<"finding points\n";
 //  //   int pointnr = 0;
 //  //   for (std::vector<Point>::iterator it = points->begin();
 //  //        it != points->end(); ++it) {
 //  //    
 //  //    points->at(pointnr).minDist = __DBL_MAX__; 
 //  //    //std::cout<<"before assigned\n";
 //  //    //std::cout<<points->at(pointnr).x<<" "<<
 //  //    //           points->at(pointnr).y<<" "<<
 //  //    //           points->at(pointnr).minDist<<" "<<
 //  //    //           points->at(pointnr).cluster<<"\n";
 //  //  
 //  //    int centerid = 0;
 //  //    for (std::vector<Point>::iterator c = centers->begin();
 //  //         c != centers->end(); ++c) {
 //  //     
 //  //     double dist = points->at(pointnr).dist2(centers->at(centerid));
 //  //     //std::cout<<"dist to: "<<centers->at(centerid).x<<","<<
 //  //     //                        centers->at(centerid).y<<" : "<<
 //  //     //                        dist<<"\n";
 //  //     if(dist < points->at(pointnr).minDist){
 //  //      points->at(pointnr).minDist=dist;
 //  //      points->at(pointnr).cluster=centerid;
 //  //     }
 //  //     centerid++;  
 //  //    }
 //  //    //std::cout<<"after assigned\n";
 //  //    //std::cout<<points->at(pointnr).x<<" "<<
 //  //    //           points->at(pointnr).y<<" "<<
 //  //    //           points->at(pointnr).minDist<<" "<<
 //  //    //           points->at(pointnr).cluster<<"\n";
 //  //    //std::cout<<"--------------\n";
 //  //    pointnr++;
 //  //   }
 //  //  }
 //  //  
 //  //  
 //  //  void initCenters(std::vector<Point>* pointlist, int ncenters, std::vector<Point>* oldcenterlist, std::vector<Point>* newcenterlist){
 //  //   //srand(time(0));  // set the seed
 //  //   for (int i = 0; i < ncenters; ++i) {
 //  //       oldcenterlist->push_back( Point(__DBL_MAX__,__DBL_MAX__) );
 //  //       newcenterlist->push_back(pointlist->at(rand() % pointlist->size() ));
 //  //   }
 //  //  }
 //  //  
 //  //  
 //  //  void recalculateCenters(std::vector<Point>* points, std::vector<Point>* centers){
 //  //  
 //  //   std::vector<int> nPoints;
 //  //   std::vector<double> sumX, sumY;
 //  //  
 //  //   // Initialise with zeroes
 //  //   for (int i = 0; i < centers->size(); ++i) {
 //  //       nPoints.push_back(0);
 //  //       sumX.push_back(0.0);
 //  //       sumY.push_back(0.0);
 //  //   }
 //  //  
 //  //   for (std::vector<Point>::iterator it = points->begin();
 //  //        it != points->end(); ++it) {
 //  //    
 //  //    Point p = *it;
 //  //    //std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
 //  //  
 //  //    nPoints[p.cluster]++;
 //  //    sumX[p.cluster] += p.x;
 //  //    sumY[p.cluster] += p.y;
 //  //  
 //  //    //p.minDist = __DBL_MAX__;
 //  //  
 //  //   } 
 //  //  
 //  //   int centerid = 0;
 //  //   for (std::vector<Point>::iterator c = centers->begin();
 //  //        c != centers->end(); ++c) {
 //  //    
 //  //    //std::cout<<" Old Center "<<std::endl;
 //  //    //std::cout<<centers->at(centerid).x<<","<<centers->at(centerid).y<<"\n";
 //  //  
 //  //    //std::cout<<sumX[centerid]<<"\n";
 //  //    //std::cout<<sumY[centerid]<<"\n";
 //  //  
 //  //    centers->at(centerid).x = sumX[centerid]/nPoints[centerid];
 //  //    centers->at(centerid).y = sumY[centerid]/nPoints[centerid];
 //  //    //std::cout<<" New Center "<<std::endl;
 //  //    //std::cout<<centers->at(centerid).x<<","<<centers->at(centerid).y<<"\n";
 //  //  
 //  //    centerid++;  
 //  //  
 //  //   }
 //  //    
 //  //  }


int main()
{

 int ncenters = 2;

 std::string filename = "triplegauss.csv";
 //std::string filename = "twoblobs.csv";

 std::vector<Point> pointlist =  getPointsFromCSV(filename);

 // std::cout<<" Points in pointlist\n";
 // for (std::vector<Point>::iterator it = pointlist.begin();
 //      it != pointlist.end(); ++it) {
 //  Point p = *it;
 //  std::cout<<"("<<p.x<<","<<p.y<<")"<<"\n";
 // }

 float maxX = -__FLT_MAX__;
 float maxY = -__FLT_MAX__;
 float minX = __FLT_MAX__;
 float minY = __FLT_MAX__;

 // std::cout<<maxX<<" "<<maxY<<"\n";
 // std::cout<<minX<<" "<<minY<<"\n";

 findRangeOfInputData( minX, minY, maxX, maxY, pointlist );

 // std::cout<<"Max Point";
 // std::cout<<maxX<<" "<<maxY<<"\n";
 // std::cout<<"Min Point";
 // std::cout<<minX<<" "<<minY<<"\n";


 std::vector<Point> centerlist;
 int ncentersX = 5;
 int ncentersY = 5;
 initializeCenters( ncentersX, ncentersY, minX, minY, maxX, maxY, centerlist );

 // for (std::vector<Point>::iterator it = centerlist.begin();
 //      it != centerlist.end(); ++it){
 //  Point center = *it;
 //  std::cout<<"("<<center.x<<","<<center.y<<")\n";
 //
 // }


 float searchradius = 10;
 associateCentersToPoints( pointlist, centerlist, searchradius );

 std::cout<<" Points in pointlist\n";
 for (std::vector<Point>::iterator it = pointlist.begin();
      it != pointlist.end(); ++it) {
  Point p = *it;
  std::cout<<"("<<p.x<<","<<p.y<<")";
  
  std::cout<<" Clusters: ";
  for (std::vector<int>::iterator itC = p.cluster.begin();
       itC != p.cluster.end(); ++itC) {

   std::cout<<*itC<<" ";
  }
  std::cout<<"\n";

 }



//  //   initCenters(&pointlist, ncenters, &oldcenterlist, &newcenterlist);
//  //  
//  //   //std::cout<<" Centers init-ed\n";
//  //   //for (int i = 0; i < ncenters; ++i) {
//  //   //  std::cout << newcenterlist[i].x << " " << newcenterlist[i].y <<std::endl;
//  //   //}
//  //  
//  //  
//  //  
//  //   int iterationnr = 0;
//  //   while(true){
//  //    associatePointsToClusters(&pointlist, &newcenterlist);
//  //  
//  //    //std::cout<<" Associated points\n";
//  //    //for (std::vector<Point>::iterator it = pointlist.begin();
//  //    //     it != pointlist.end(); ++it) {
//  //    // Point p = *it;
//  //    // std::cout<<p.x<<" "<<p.y<<" "<<p.minDist<<" "<<p.cluster<<"\n";
//  //    // 
//  //    //}
//  //  
//  //    recalculateCenters(&pointlist, &newcenterlist);
//  //  
//  //    //std::cout << newcenterlist.size() <<std::endl;
//  //    //for (int i = 0; i < newcenterlist.size(); ++i) {
//  //    //  std::cout << newcenterlist[i].x << " " << newcenterlist[i].y <<std::endl;
//  //    //}
//  //  
//  //    double diffX = 0;
//  //    double diffY = 0;
//  //    for (int i = 0; i < newcenterlist.size(); ++i) {
//  //      diffX += newcenterlist[i].x - oldcenterlist[i].x;
//  //      diffY += newcenterlist[i].y - oldcenterlist[i].y;
//  //    }
//  //    //std::cout<<" Diffs "<<diffX<<" "<<diffY<<"\n";
//  //    //std::cout<<std::abs(diffX+diffY)<<"\n";
//  //  
//  //    //write to file
//  //    std::ofstream myfile;
//  //    std::string filename = "./plots/outfile_points"+std::to_string(iterationnr)+".csv";
//  //    myfile.open(filename);
//  //    myfile << "x,y,c" << std::endl;
//  //    
//  //    for (std::vector<Point>::iterator it = pointlist.begin(); 
//  //         it != pointlist.end(); ++it) {
//  //     myfile << it->x << "," << it->y << "," << it->cluster << std::endl;
//  //    }
//  //    myfile.close();
//  //  
//  //    filename = "./plots/outfile_centers"+std::to_string(iterationnr)+".csv";
//  //    myfile.open(filename);
//  //    myfile << "x,y" << std::endl;
//  //    
//  //    for (std::vector<Point>::iterator it = newcenterlist.begin(); 
//  //         it != newcenterlist.end(); ++it) {
//  //     myfile << it->x << "," << it->y << std::endl;
//  //    }
//  //    myfile.close();
//  //  
//  //    if(std::abs(diffX+diffY) < 0.1) break;
//  //  
//  //    for (int i = 0; i < newcenterlist.size(); ++i) {
//  //      oldcenterlist[i].x = newcenterlist[i].x;
//  //      oldcenterlist[i].y = newcenterlist[i].y;
//  //    }
//  //    
//  //   iterationnr++;
//  //  
//  //   }
//  //  
//  //   std::cout<<"----------------------\n";
//  //   std::cout<<"Final Centers:\n";
//  //   for (std::vector<Point>::iterator it = newcenterlist.begin(); 
//  //        it != newcenterlist.end(); ++it) {
//  //    std::cout << " (" << it->x << "," << it->y << ") \n"; 
//  //   }
//  //   std::cout<<"Iterations: "<<iterationnr<<"\n";
//  //   std::cout<<"----------------------\n";


}

