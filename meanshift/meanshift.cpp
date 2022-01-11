// Mean Shift Clustering Algorithm

#include <ctime>     // for a random seed
#include <fstream>   // for file-reading
#include <iostream>  // for stdio
#include <vector>
#include <cmath>     // for abs
#include <limits>    // for initializing to max/min

struct Point {
    double x, y;                // coordinates
    std::vector<int> cluster;   // associated cluster(s)
    // double minDist;             // distance(2) to nearest cluster

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


void associatePointsToCenters( std::vector<Point>& pointlist,
     std::vector<Point>& centerlist, float searchradius ){

 // for each point, see if center_i is within searchradius
 // if so, add it to the list
 int pointnr = 0;
 int centernr = 0;
 for (std::vector<Point>::iterator itCenter = centerlist.begin();
      itCenter != centerlist.end(); ++itCenter) {
  for (std::vector<Point>::iterator itPoint = pointlist.begin();
       itPoint != pointlist.end(); ++itPoint) {

  // std::cout<<"Point:  ("<<itPoint->x<<","<<itPoint->y<<")\n";
  // std::cout<<"Center: ("<<itCenter->x<<","<<itCenter->y<<")\n\n";
  if( itPoint->dist2(*itCenter) < searchradius*searchradius )
   centerlist.at(centernr).cluster.push_back( pointnr );
   // std::cout<<pointlist.at(pointnr).x<<" "<<pointlist.at(pointnr).y<<"\n\n";
   // std::cout<<centerlist.at(centernr).x<<" "<<centerlist.at(centernr).y<<"\n\n";
 
  pointnr++;
  }
 pointnr = 0;
 centernr++;
 }

}


void recalculateCenters( std::vector<Point>& pointlist,
                         std::vector<Point>& centerlist,
                         bool& haveweconverged ){

 int pointnr = 0;
 int centernr = 0;

 std::vector<Point> newcenterlist;
 std::vector<Point> cleanednewcenterlist;

 //std::cout<<"Old Centers\n";
 for (std::vector<Point>::iterator itC = centerlist.begin();
      itC != centerlist.end(); ++itC) {
 
  int nrpoints = 0;
  float totalX = 0;
  float totalY = 0;
  // std::cout<<"("<<itC->x<<","<<itC->y<<")\n";
  // std::cout<<centerlist.at(centernr).x<<","<<centerlist.at(centernr).y<<"\n";
 
  for (std::vector<int>::iterator itP = itC->cluster.begin();
       itP != itC->cluster.end(); ++itP) {
   nrpoints++;
   totalX += pointlist.at(*itP).x;
   totalY += pointlist.at(*itP).y;
  //  std::cout<<": ("<<pointlist.at(*itP).x<<","<<pointlist.at(*itP).y<<")";
  }

  if(nrpoints>0){
   newcenterlist.push_back( Point( totalX/nrpoints, totalY/nrpoints ) );
  }

  centernr++;
 }

 //std::cout<<"New Centers\n";
 //for (std::vector<Point>::iterator itCenter = newcenterlist.begin();
 //     itCenter != newcenterlist.end(); ++itCenter) {
 //  std::cout<<" ("<<itCenter->x<<","<<itCenter->y<<")\n";
 //}


 // remove overlapping centers
 for ( int i=0; i<newcenterlist.size(); ++i ){
  //std::cout<<i<<"\n";
  bool keepcenter = true;
  for ( int j=i+1; j<newcenterlist.size(); ++j ){
   if(i==j) continue;

   float d2 = newcenterlist[i].dist2(newcenterlist[j]);
   //std::cout<<"d2 "<<d2<<"\n";
   if(d2 < 4) keepcenter=false;
   //std::cout<<" "<<j<<"\n";
  }
  if(keepcenter) cleanednewcenterlist.push_back(newcenterlist[i]);
 }

 // test for convergence
 // std::cout<<"Testing for convergence\n";
 // std::cout<<centerlist.size()<<" "<<cleanednewcenterlist.size()<<"\n"; 
 if(centerlist.size() == cleanednewcenterlist.size()){
  float deltaX = 0;
  float deltaY = 0;
  for ( int i=0; i<centerlist.size(); ++i ){
    // std::cout<<" old ("<<centerlist.at(i).x<<","<<centerlist.at(i).y<<")\n";
    // std::cout<<" new ("<<cleanednewcenterlist.at(i).x<<","<<cleanednewcenterlist.at(i).y<<")\n\n";
    deltaX += std::fabs( centerlist.at(i).x - cleanednewcenterlist.at(i).x );
    deltaY += std::fabs( centerlist.at(i).y - cleanednewcenterlist.at(i).y );
  }
  // std::cout<<" DeltaX: "<<deltaX<<"\n";
  // std::cout<<" DeltaY: "<<deltaY<<"\n";
  if( (deltaX+deltaY) < 0.1 ) haveweconverged = true;
 }

 centerlist = cleanednewcenterlist;

}

 
void writeToFile( std::vector<Point>& thelist, std::string filebase, 
                  std::string datatype, int iterationnr, bool docolor ){

 std::ofstream myfile;
 std::string filename = filebase+datatype+std::to_string(iterationnr)+".csv";
 myfile.open(filename);
 
 if (docolor)  myfile << "x,y,c" << std::endl;
 else          myfile << "x,y" << std::endl;

 for (std::vector<Point>::iterator it = thelist.begin(); 
      it != thelist.end(); ++it) {

  if(docolor) 
   myfile << it->x << "," << it->y << "," << it->cluster[0] << std::endl;
  else
   myfile << it->x << "," << it->y << "\n";
  }
 myfile.close();



}

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


// associate points to custer centers
//associatePointsToCluster( pointlist, centerlist );
void associateCentersToPoints(std::vector<Point>& pointlist,
                              std::vector<Point>& centerlist){

 // for each point, find the nearest center

 //std::cout<<"finding points\n";
 int pointnr = 0;
 for (std::vector<Point>::iterator it = pointlist.begin();
      it != pointlist.end(); ++it) {
  
  float minDist = __FLT_MAX__;  
  pointlist.at(pointnr).cluster.clear();
  pointlist.at(pointnr).cluster.push_back(-1);
  // std::cout<<"before assigned\n";
  // std::cout<<pointlist.at(pointnr).x<<" "<<
  //            pointlist.at(pointnr).y<<"\n";

  int centerid = 0;
  for (std::vector<Point>::iterator c = centerlist.begin();
       c != centerlist.end(); ++c) {
   
   double dist = pointlist.at(pointnr).dist2(centerlist.at(centerid));
   //std::cout<<"dist to: "<<centerlist.at(centerid).x<<","<<
   //                        centerlist.at(centerid).y<<" : "<<
   //                        dist<<"\n";
   if(dist < minDist){
    minDist=dist;
    pointlist.at(pointnr).cluster[0]=centerid;
   }
   centerid++;  
  }
  // std::cout<<"after assigned\n";
  // std::cout<<pointlist.at(pointnr).x<<" "<<
  //            pointlist.at(pointnr).y<<" "<<
  //            //pointlist.at(pointnr).minDist<<" "<<
  //            pointlist.at(pointnr).cluster[0]<<"\n";
  // std::cout<<"--------------\n";
  pointnr++;
 }

}
  

int main()
{

 std::string infilename = "./data/fourgauss.csv";

 std::vector<Point> pointlist =  getPointsFromCSV(infilename);

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


 int iterationnr = 0;
 bool weveconverged = false;
 std::string filebase = "./plots/outfile_";

 while(true){

  if (iterationnr >= 50) break;  // just in case 
  if (weveconverged) break; 
  // write centers to file
  writeToFile( centerlist, filebase, "centers", iterationnr, false ); 
 
  float searchradius = 15;
  associatePointsToCenters( pointlist, centerlist, searchradius );
 
  // std::cout<<"--Original Centers--\n";
  // for (std::vector<Point>::iterator itC = centerlist.begin();
  //      itC != centerlist.end(); ++itC) {
  // 
  //  std::cout<<"("<<itC->x<<","<<itC->y<<")";
  // 
  //   for (std::vector<int>::iterator itP = itC->cluster.begin();
  //        itP != itC->cluster.end(); ++itP) {
  // 
  //    std::cout<<": ("<<pointlist.at(*itP).x<<","<<pointlist.at(*itP).y<<")";
  // 
  //   }
  //  std::cout<<"\n";
  // }
 
  recalculateCenters( pointlist, centerlist, weveconverged );
 
  //std::cout<<"Converged: "<<weveconverged<<"\n";
  // std::cout<<"--New Centers--\n";
  // for (std::vector<Point>::iterator itC = centerlist.begin();
  //      itC != centerlist.end(); ++itC) {
  // 
  //  std::cout<<"("<<itC->x<<","<<itC->y<<")\n";
  // 
  // }

  iterationnr++;

 }

 // associate points to custer centers
 associateCentersToPoints( pointlist, centerlist);

 // std::cout<<" Points in pointlist\n";
 // for (std::vector<Point>::iterator it = pointlist.begin();
 //      it != pointlist.end(); ++it) {
 //  Point p = *it;
 //  std::cout<<"("<<p.x<<","<<p.y<<") "<<p.cluster[0]<<"\n";
 // }

 // write points to file
 writeToFile( pointlist, filebase, "points", 0, true ); 

 std::cout<<"----------------------\n";
 std::cout<<"Final Centers:\n";
 for (std::vector<Point>::iterator it = centerlist.begin(); 
      it != centerlist.end(); ++it) {
  std::cout << " (" << it->x << "," << it->y << ") \n"; 
 }
 std::cout<<"Iterations: "<<iterationnr<<"\n";
 std::cout<<"----------------------\n";

}




