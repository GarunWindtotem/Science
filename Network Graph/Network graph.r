# Libraries
library(tidyverse)
library(viridis)
library(patchwork)
library(hrbrthemes)
library(ggraph)
library(igraph)
library(networkD3)

# Load researcher data
dataUU <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/13_AdjacencyUndirectedUnweighted.csv", header=TRUE)

# Transform the adjacency matrix in a long format
connect <- dataUU %>% 
  gather(key="to", value="value", -1) %>%
  na.omit()

# Number of connection per person
c( as.character(connect$from), as.character(connect$to)) %>%
  as.tibble() %>%
  group_by(value) %>%
  summarize(n=n()) -> coauth
colnames(coauth) <- c("name", "n")

# NetworkD3 format
graph=simpleNetwork(connect)

# Plot
simpleNetwork(connect,     
        Source = 1,                 # column number of source
        Target = 2,                 # column number of target
        height = 880,               # height of frame area in pixels
        width = 1980,
        linkDistance = 10,         # distance between node. Increase this value to have more space between nodes
        charge = -4,              # numeric value indicating either the strength of the node repulsion (negative value) or attraction (positive value)
        fontSize = 5,              # size of the node names
        fontFamily = "serif",       # font og node names
        linkColour = "#666",        # colour of edges, MUST be a common colour for the whole graph
        nodeColour = "#69b3a2",     # colour of nodes, MUST be a common colour for the whole graph
        opacity = 0.9,              # opacity of nodes. 0=transparent. 1=no transparency
        zoom = T                    # Can you zoom on the figure?
        )