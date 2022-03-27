package main

import (
	"context"
	"fmt"
	"net"
	"os"

	"github.com/NRI.service/internal/pb"
	"github.com/rs/zerolog"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

var availability = map[string][]string{
	"Lenina":  {"1", "2", "3"},
	"Gorkova": {"1a", "2a", "3a"},
}
var url = "https://test.equip.com/"

func main() {
	logger := zerolog.New(os.Stdout).With().Timestamp().Logger()
	grpcServer := grpc.NewServer()
	pb.RegisterNRIServer(grpcServer, &server{})
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", 8080))
	if err != nil {
		logger.Fatal().Err(err).Msg("Listening gRPC error")
	}
	logger.Info().Msgf("GRPC server is listening on :%d", 8080)
	err = grpcServer.Serve(lis)
	if err != nil && err != grpc.ErrServerStopped {
		logger.Fatal().Err(err).Msg("GRPC server error")
	}

}

// Default implementation of the MyApp server interface
type server struct {
	pb.UnimplementedNRIServer
}

func (s *server) Check(ctx context.Context, req *pb.ServiceRequest) (*pb.ServiceResponse, error) {
	resp := consist(*req)
	if resp.EquipmentUrl == "" {
		return &pb.ServiceResponse{}, status.Errorf(codes.InvalidArgument, "invalid request payload")
	}
	return &resp, nil
}

func consist(req pb.ServiceRequest) pb.ServiceResponse {
	for k, _ := range availability {
		if k == req.Street {
			for _, v := range availability[k] {
				if v == req.House {
					return pb.ServiceResponse{EquipmentUrl: url}
				}
			}
		}
	}
	return pb.ServiceResponse{}
}

// func GRPCConnect() (*grpc.ClientConn, error) {
// 	var opts []grpc.DialOption
// 	opts = append(opts, grpc.WithInsecure())
// 	addr := viper.GetString("server.address.full")
// 	conn, err := grpc.Dial(addr, opts...)
// 	if err != nil {
// 		return nil, err
// 	}
// 	return conn, nil
// }
