#include<bits/stdc++.h>
using namespace std;
const int MAX = 1e6-1;
int parent_vertex[MAX];
int find_function(int p)
{
    while(parent_vertex[p]!=p)
    {
       parent_vertex[p] = parent_vertex[parent_vertex[p]];
       p = parent_vertex[p];

    }
    return p;
}
void merge_subsets_function(int i,int j)
{
    int m = find_function(i);
    int n = find_function(j);
    parent_vertex[m] =parent_vertex[n];
}
int main()
{
    int total_vertices;
    cout<<"Enter total vertices: ";
    cin>>total_vertices;
    int total_edges;
    cout<<"Enter total edges: ";
    cin>>total_edges;
    vector<pair<int,pair<int,int>>>adjency_list;
    cout<<"Enter weight: source_vertex: destination_vertex: \n";
    for(int x=0;x<total_edges;x++)
    {
        int weight_of_edges;
        int source_vertex,destination_vertex;
        cin>>weight_of_edges>>source_vertex>>destination_vertex;
        adjency_list.push_back({weight_of_edges,{source_vertex,destination_vertex}});
    }
    sort(adjency_list.begin(),adjency_list.end());
    for(int x = 0;x<MAX;x++)
    {
        parent_vertex[x] = x;
    }
    vector<pair<int,int>>edges_of_tree_;
    int total_weight = 0;
    for(auto x:adjency_list)
    {
        int y = x.second.first;
        int z = x.second.second;
        int minimum_spanning_cost = x.first;
        if(find_function(y)!=find_function(z))
        {
            total_weight+= minimum_spanning_cost;
            merge_subsets_function(y,z);
            edges_of_tree_.push_back({y,z});
        }
    }
    cout<<"Edges source_vertex destination_vertex : "<<endl;
    for(auto x:edges_of_tree_)
    {
        cout<<x.first<<" "<<x.second<<endl;
    }
    cout<<"Total weight of Minimum Spanning Tree = ";
    cout<<total_weight<<endl;
    return 0;
}
